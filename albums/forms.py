from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artists',
            'created_at',
        ]

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'name',
        ]