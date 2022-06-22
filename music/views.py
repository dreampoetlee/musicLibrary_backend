from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import SongSerializer
from . models import Song

# Create your views here.
@api_view(['GET', 'POST'])
def song_library(request):
  if request.method == 'GET':
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serializer = SongSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def song_detail(request, pk):
  song = get_object_or_404(Song, pk=pk)
  if request.method == 'GET':
    serializer = SongSerializer(song)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    serializer = SongSerializer(song, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'DELETE':
    serializer = SongSerializer(song)
    song.delete()
    return_value = serializer.data
    return_value['id'] = pk
    return Response(return_value, status=status.HTTP_200_OK)
  elif request.method == 'PATCH':
    serializer = SongSerializer(song, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)