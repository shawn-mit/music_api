from rest_framework import serializers
from musicmvc.models import *


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    """
    The Purpose of this serializer is for the Album model to JSON.

    """

    class Meta:
        model = Album
        fields = ('url', 'id', 'first_name', 'last_name',
                  'artist_id', 'genre_id', 'title', 'release_date',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    """
            The Purpose of this serializer is for the Artist model to JSON. 

    """

    class Meta:
        model:
            Aritst
        fields = ('url', 'id', 'first_name', 'last_name', 'year_established', 'age',)
 


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    """
    The purpose of this serializer is for the Genre model to JSON. 



    """

    class Meta:
        model = Genre
        fields = ('url', 'id', 'label',)


class SongSerializer(serializers.HyperlinkedModelSerializer):

    """
    The Purpose of this serializer is for the Song model to JSON.
    """
    class Meta:

        model = Song
        fields = ('url', 'id', 'title', 'song_length','release_date', 'genre_id', 'artist_id', 'album_id',)