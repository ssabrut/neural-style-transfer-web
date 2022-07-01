from django.shortcuts import render
from django.http import HttpResponse
from index.models import Content, Style
from .artist import *

# Create your views here.
def index(request, content_id, style_id):
  content_img = Content.objects.get(id=content_id)
  style_img = Style.objects.get(pk=style_id)
  return render(request, 'canvas.html')