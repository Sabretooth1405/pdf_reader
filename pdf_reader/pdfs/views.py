from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    
)
from .models import File,Text
from .forms import FileCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from PIL import Image,ImageFilter
from pdf2image import convert_from_path
import pytesseract
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

#function that handles conversion from pdf/img to text
#pytessaract is used for OCR purposes
def convert(filepath):
    txt = ""
    #options for diffrent file formats as last 3 or 4 parts of the filepath represents the file extension
    if filepath[-3:]=="pdf":
        doc = convert_from_path(filepath)
        for im in doc:
            txt += pytesseract.image_to_string(im)
            txt += '\n'
    elif filepath[-3:] in ['jpg', 'png'] or filepath[-4:] in ['jpeg','webp']:
        im = Image.open(filepath)
        txt = pytesseract.image_to_string(im)
    else:
        #in case of unsupported filetypes
        txt="file not supported"
    return txt

# File Upload view.Login is required
@login_required(login_url='/login/')
def file_upload_view(req):
    if req.method == 'POST':
        form = FileCreateForm(req.POST, req.FILES)
        if form.is_valid():
            #i f form is valid then save the file and make the text using convert function
            file=form.save(commit=False)
            file.user=req.user
            form.save()
            # document.name is of the form document/filename
            name=file.document.name.split('/')[1]
            path=file.document.name
            # PDF_ROOT is defined in settings it would be changed in prod
            path = settings.PDF_ROOT+path
            converted_text=convert(path)
            # creating instance of Text model
            new_text = Text(text=converted_text, file_name=name, file_associated=file)
            new_text.save()
            id=new_text.pk
            # redirect to created post
            return redirect(f'/detail/{id}')
    else:
        form = FileCreateForm()
    return render(req, 'pdfs/file_upload_form.html', {
        'form': form
    })

# View to list all texts with the file and link to it
#A truncated form of the text is shown in the list view
# TODO: add pagination
class TextListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Text
    template_name = 'pdfs/text_list.html'  
    context_object_name = 'texts'
    # restrict texts to that which have been made from files uploaded by the user
    def get_queryset(self):
        queryset = super(TextListView, self).get_queryset()
        queryset = queryset.filter(file_associated__user__username=self.request.user)
        return queryset
# Show the formatted text in detail with the file and link to it

class TextDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Text
    template_name='pdfs/text_detail.html'
    context_object_name='text'
 # testing function for userpassestestmixim to ensure acces only to user which has created the view
    def test_func(self):
        text = self.get_object()
        if self.request.user == text.file_associated.user:
            return True
        return False
