from django import forms
from django.contrib.auth.models import User
from .models import File
class FileCreateForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'document', )
