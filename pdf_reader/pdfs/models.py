from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}- File'



class Text(models.Model):
    text = models.TextField(default='default')
    file_name = models.CharField(max_length=255)
    file_associated=models.OneToOneField(File,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file_name}- text'



