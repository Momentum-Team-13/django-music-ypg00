from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Album

def list_albums(request):
    # albums = Album.objects.all()
    return render(request, "base.html")

def create_album(request):
    pass
