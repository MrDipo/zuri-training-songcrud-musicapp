from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + self.last_name
    

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_released = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.song_id