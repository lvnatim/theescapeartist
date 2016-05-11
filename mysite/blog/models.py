from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    img_path = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    date = models.CharField(max_length=20)
    datestamp = models.DateField()
    text = models.TextField()
    draft= models.BooleanField(default=False)

    def __str__(self):
        return self.title
