from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
  if request.method == 'POST':
    content_form = ContentForm(request.POST, request.FILES)
    if content_form.is_valid():
      content_form.save()
      content_img = content_form.instance
      return render(request, 'index.html', {
        'content_form': content_form,
        'content_img': content_img
      })
  else:
    content_form = ContentForm()
  return render(request, 'index.html', {
    'content_form': content_form
  })