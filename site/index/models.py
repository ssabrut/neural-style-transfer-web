from django.db import models

# Create your models here.
class Art(models.Model):
  content_image = models.ImageField(upload_to='images/')