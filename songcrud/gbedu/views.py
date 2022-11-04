from django.shortcuts import render
from rest_framework import viewsets
from musicapp.models import Artiste, Song, Lyric
from gbedu.serializers import ArtisteSerializer, SongSerializer, LyricSerializer


class ArtisteViewSet(viewsets.ModelViewSet):
   queryset = Artiste.objects.all()
   serializer_class = ArtisteSerializer


class SongViewSet(viewsets.ModelViewSet):
   queryset = Song.objects.all()
   serializer_class = SongSerializer


class LyricViewSet(viewsets.ModelViewSet):
   queryset = Lyric.objects.all()
   serializer_class = LyricSerializer