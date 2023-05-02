from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.widgets

class Editor(models.Model):
    body = RichTextField(blank=True, null=True)