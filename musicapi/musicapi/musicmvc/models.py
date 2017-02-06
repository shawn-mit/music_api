from django.db import models


# Create your models here.

class Artist(models.Model):
    """
        Artists model class
        The purpose of this class is to define 
        author: Shawn
        methods: __str__ Returns a string
        subclasss: meta - ordering by year_established
    """
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    year_established = models.IntegerField(max_length=4)
    age = models.IntegerField(max_length=3)

    class Meta:
        ordering = ('year_established',)

    def __str__(self):
        return '{} {} {} {}'.format(self.first_name, self.last_name, self.year_established, self.age,)


class Genre(models.Model):

    label = models.CharField(max_length=50)
    subgenre = models.CharField(max_length=50)

    class Meta: 
        ordering = ('subgenre',)

    def __str__(self):
            return '{}'.format(self.label,)

class Album(models.Model):
    """
        Albums model class
        Purpose of this class is to define Albums
        returns a string
        subclass: meta - ordering by title 
    """

    title = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    release_date = models.DateField()
    artist= models.ForeignKey(Artist, null=True)
    genre = models.ForeignKey(Genre, null=True)

    class Meta: 
        ordering =('title',)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.title, self.label,self.artist, self.release_date, self.genre,)

class Song(models.Model):

    """ 
        Song model of class
        Purpose of this class is to define  the Songs of the artists
        author: Shawn
        method: __str__
        subclass : meta ordering by title 

    """

    title = models.CharField(max_length=50)
    song_length = models.IntegerField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, null=True)
    album = models.ForeignKey(Album, null=True)

    class Meta: 
        ordering = ('title',)

    def __str__ (self):
            return '{} {} {} {} {} {}'.format(self.title, self.song_length,self.release_date, self.genre, self.artist,self.album,)