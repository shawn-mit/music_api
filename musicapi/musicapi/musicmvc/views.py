from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
from .models import *
from .serializers import *
from rest_framework import viewsets 

# Create your views here.
class JSONResponse(HttpResponse):

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)



class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


