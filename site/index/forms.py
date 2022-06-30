from dataclasses import field
from django import forms
from .models import *

class ContentForm(forms.ModelForm):
  class Meta:
    model = Content
    fields = ['content_img']
    widgets = {
      'content_img': forms.FileInput(attrs={'id': 'content_image'})
    }

class StyleForm(forms.ModelForm):
  class Meta:
    model = Style
    fields = ['style_img']
    widgets = {
      'style_img': forms.FileInput(attrs={'id': 'style_image'})
    }