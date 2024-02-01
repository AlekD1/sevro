from django.shortcuts import render
from rest_framework import viewsets

from mixins.viewset_mixins import SerializerClassesMixin
from .serializers import AlbumListSerializer, AlbumRetrieveSerializer
from .models import Album


class AlbumViewSet(SerializerClassesMixin, viewsets.ReadOnlyModelViewSet):
    LIST = AlbumListSerializer
    RETRIEVE = AlbumRetrieveSerializer
    queryset = Album.objects.prefetch_related('images').all()