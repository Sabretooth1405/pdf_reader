from django.db import models
from django.contrib.auth.models import User
import os
from  django.core.exceptions import ValidationError

def validate_file_extension(value):
  
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.pdf', '.jpg','.jpeg','.png','.webp','.tiff']
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(
        upload_to='documents/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}- File'



class Text(models.Model):
    text = models.TextField(default='default')
    file_name = models.CharField(max_length=255)
    file_associated=models.OneToOneField(File,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file_name}- text'



