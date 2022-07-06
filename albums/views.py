from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist

def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})

def add_album(request):
    return render(request, 'albums/add_album.html')

def add_artist(request):
    return render(request, 'artists/add_artist.html')
