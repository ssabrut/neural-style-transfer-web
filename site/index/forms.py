from dataclasses import field
from django import forms
from .models import *

class ContentForm(forms.ModelForm):
  class Meta:
    model = Art
    fields = ['content_image']
    widgets = {
      'content_image': forms.FileInput(attrs={'id': 'content-image'})
    }
