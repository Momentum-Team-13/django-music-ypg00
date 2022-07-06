from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from albums import views as album_views

# URLconf
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
    
    # Home
    path('', album_views.list_albums, name='list_albums'),

    # Album
    path('albums/new/', album_views.add_album, name='add_album'),
    path('albums/<int:pk>/', album_views.album_detail, name='album_detail'),
    path('albums/<int:pk>/edit', album_views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete', album_views.delete_album, name='delete_album'),

    # Artist
    path('artists/', album_views.add_artist, name='add_artist'),
]