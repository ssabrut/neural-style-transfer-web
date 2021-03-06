from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
  if request.method == 'POST':
    content_form = ContentForm(request.POST, request.FILES)
    style_form = StyleForm(request.POST, request.FILES)
    if content_form.is_valid() and style_form.is_valid():
      content_form.save()
      style_form.save()
      images = [content_form.instance.content_img, style_form.instance.style_img]
      return redirect('canvas/', {
        'content_form': content_form,
        'style_form': style_form,
        'images': images,
      })
  else:
    content_form = ContentForm()
    style_form = StyleForm()
  return render(request, 'index.html', {
    'content_form': content_form,
    'style_form': style_form,
  })

def canvas(request):
  return render(request, 'canvas.html')