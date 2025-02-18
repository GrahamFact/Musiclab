from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField(blank=True, null=True)
    cover_image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    created_at = models.DateTimeField(auto_now_add=True)
    artists = models.ManyToManyField(Artist, related_name="songs")
    genres = models.ManyToManyField(Genre, related_name="songs")

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, related_name="playlists")

    def __str__(self):
        return f"{self.name} - {self.user.username}"
