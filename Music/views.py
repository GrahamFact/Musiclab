from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Artist, Album, Song


# Получение списка всех артистов
def artist_list(request):
    artists = Artist.objects.all().values()
    return JsonResponse(list(artists), safe=False)


# Получение деталей одного артиста
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return JsonResponse({
        "id": artist.id,
        "name": artist.name,
        "bio": artist.bio,
        "birth_date": artist.birth_date,
        "albums": list(artist.albums.values("id", "title", "release_date")),
        "songs": list(artist.songs.values("id", "title", "album_id", "release_date"))
    })


# Получение списка альбомов
def album_list(request):
    albums = Album.objects.all().values()
    return JsonResponse(list(albums), safe=False)


# Получение деталей альбома
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return JsonResponse({
        "id": album.id,
        "title": album.title,
        "artist": album.artist.name,
        "release_date": album.release_date,
        "songs": list(album.songs.values("id", "title", "duration"))
    })


# Получение списка песен
def song_list(request):
    songs = Song.objects.all().values()
    return JsonResponse(list(songs), safe=False)


# Получение деталей песни
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return JsonResponse({
        "id": song.id,
        "title": song.title,
        "artist": song.artist.name,
        "album": song.album.title if song.album else None,
        "duration": song.duration,
        "release_date": song.release_date
    })
