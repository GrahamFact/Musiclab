from django.contrib.auth.models import Group, User
from rest_framework import serializers


from Music.models import Artist, Album, Genre, Song, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'date_joined']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
