"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from albums import views as album_views

# URL Configurations
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
    
    # Home
    path('', album_views.list_albums, name='list_albums'),

    # Child URLs
    path('albums/', album_views.add_album, name='add_album'),
    path('artists/', album_views.add_artist, name='add_artist'),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),

#         # For django versions before 2.0:
#         # url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
