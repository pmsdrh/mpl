from django.db import models

# Create your models here.

class PlayList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(mex_length=50, null=False, default="")
