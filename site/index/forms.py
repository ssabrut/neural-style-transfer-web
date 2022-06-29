from dataclasses import field
from django import forms
from .models import *

class ArtForm(forms.ModelForm):
  class Meta:
    model = Art
    fields = ['image']