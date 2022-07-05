from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist

def list_albums(request):
    albums = Album.objects.all()
    artists = Artist.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums, 'artists': artists})

def create_album(request):
    pass
