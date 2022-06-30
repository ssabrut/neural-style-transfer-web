from django.db import models

# Create your models here.
class Content(models.Model):
  content_img = models.ImageField(upload_to='images/')

class Style(models.Model):
  style_img = models.ImageField(upload_to='images/')