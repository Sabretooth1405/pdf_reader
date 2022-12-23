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


def file_upload_view(req):
    if req.method == 'POST':
        form = FileCreateForm(req.POST, req.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.user=req.user
            form.save()
            name=file.document.name.split('/')[1]
            new_text = Text(text="testing", file_name=name, file_associated=file)
            new_text.save()

            return redirect('about')
    else:
        form = FileCreateForm()
    return render(req, 'pdfs/file_upload_form.html', {
        'form': form
    })
