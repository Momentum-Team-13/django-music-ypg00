from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='title', null=True, blank=True)
    # artist = models.ManyToManyField('Artist', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='artist_name', null=True, blank=True)
    # album = models.ManyToManyField(Album, null=True, blank=True)

    def __str__(self):
        return self.artist_name

