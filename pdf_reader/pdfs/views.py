from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import File,Text
from .forms import FileCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os
from django.conf import settings
def convert(filepath):
    
    doc = convert_from_path(filepath)
    
    txt=""
    
    for im in doc:
        txt += pytesseract.image_to_string(im)
        txt+='\n'
    
    return txt


def file_upload_view(req):
    if req.method == 'POST':
        form = FileCreateForm(req.POST, req.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.user=req.user
            form.save()
            name=file.document.name.split('/')[1]
            path=file.document.name
            path = settings.PDF_ROOT+path
            print(path)
            
            converted_text=convert(path)
            new_text = Text(text=converted_text, file_name=name, file_associated=file)
            new_text.save()

            return redirect('about')
    else:
        form = FileCreateForm()
    return render(req, 'pdfs/file_upload_form.html', {
        'form': form
    })


class TextListView(LoginRequiredMixin,ListView):
    model = Text
    template_name = 'pdfs/text_list.html'  
    context_object_name = 'texts'

    def get_queryset(self):
        queryset = super(TextListView, self).get_queryset()
        queryset = queryset.filter(file_associated__user__username=self.request.user)
        print(queryset)
        return queryset

class TextDetailView(LoginRequiredMixin,DetailView):
    model=Text
    template_name='pdfs/text_detail.html'
    context_object_name='text'