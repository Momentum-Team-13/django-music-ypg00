from django.shortcuts import render, redirect, get_object_or_404
from .models import Album

def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})

def create_album(request):
    pass
