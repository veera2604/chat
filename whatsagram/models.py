from django.db import models


# Create your models here.

class Chat1(models.Model):
    msg=models.TextField()
    user=models.CharField(max_length=25)
class Chat2(models.Model):
    msg=models.TextField()
    user=models.CharField(max_length=25)

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()