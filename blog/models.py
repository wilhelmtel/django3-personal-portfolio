from django.db import models
# from django.db.models import Model
## from datetime import datetime, date


class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=300)
    date=models.DateField(blank=True)
    ## date=models.DateField(auto_now_add=True,auto_now=False)
    urls=models.URLField(blank=True)
    image=models.ImageField(upload_to='portfolio/images/', blank=True)

    def __str__(self):
        return self.title

class Trails(models.Model):
    title=models.CharField(max_length=60)
    urls=models.URLField(blank=True)

    def __str__(self):
        return self.title

class MyTunes(models.Model):
    title=models.CharField(max_length=60)
    sound_file=models.FileField(upload_to='static/music/', blank=True)

    def __str__(self):
        return self.title
