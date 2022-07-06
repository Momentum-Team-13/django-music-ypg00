from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, 'albums/add_album.html', {'form': form})

def add_artist(request):
    if request.method == 'GET':
        form = ArtistForm()
    else:
        form = ArtistForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, 'artists/add_artist.html', {'form': form})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {"album": album, "form": form})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_album.html", {"album": album})