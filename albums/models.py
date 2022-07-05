from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField('Artist', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    albums = models.ManyToManyField(Album, null=True, blank=True)

    def __str__(self):
        return self.artist_name

