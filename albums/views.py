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
    # artists = album.artists
    return render(request, 'albums/album_detail.html', {'album': album})



# def edit_contact(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'GET':
#         form = ContactForm(instance=contact)
#     else:
#         form = ContactForm(data=request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_contacts')

#     return render(request, "contacts/edit_contact.html", {
#         "form": form,
#         "contact": contact
#     })

# def delete_contact(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.delete()
#         return redirect(to='list_contacts')

#     return render(request, "contacts/delete_contact.html", {"contact": contact})


# def add_note(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'GET':
#         form = NoteForm()
#     else:
#         form = NoteForm(data=request.POST)
#         if form.is_valid():
#             new_note = form.save(commit=False)
#             new_note.contact = contact
#             new_note.save()
#             return redirect(to='contact_detail', pk=pk)

#     return render(request, "contacts/notes.html", {"contact": contact, "form": form}) 

# def delete_note(request, pk):
#     note = get_object_or_404(Note, pk=pk)
#     contact_pk = note.contact.pk
#     if request.method == 'POST':
#         note.delete()
#         return redirect(to='contact_detail', pk=contact_pk)