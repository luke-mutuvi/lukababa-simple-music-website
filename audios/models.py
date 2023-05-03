from django.db import models



class Music(models.Model):

    name = models.TextField()
    playlist = models.FileField(upload_to='media/')
    video = models.FileField(upload_to='media/')
    # image= models.ImageField(upload_to='media/photos/')
# Create your models here.
    