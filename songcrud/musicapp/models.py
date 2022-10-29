from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_released = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    #artiste_id = models.CharField(max_length=30, unique=True)
    

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    #song_id = models.CharField(max_length=30, unique=True)