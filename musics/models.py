from django.db import models

# Create your models here.

class PlayList(models.Model):
    name = models.CharField(max_length=200, null=False, default="-")
    description = models.TextField()
    slug = models.SlugField(max_length=50, null=False, default="")

class Music(models.Model):
    name = models.CharField(max_length=200)
    caption = models.TextField()
    link = models.TextField()

