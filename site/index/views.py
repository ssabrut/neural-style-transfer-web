from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = ArtForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img = form.instance
      return render(request, 'index.html', {'form': form, 'img': img})
  else:
    form = ArtForm()
  return render(request, 'index.html', {'form': form})