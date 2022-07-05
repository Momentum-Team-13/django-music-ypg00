from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            
        ]

class Artist(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            
        ]