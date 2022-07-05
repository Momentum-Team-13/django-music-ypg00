from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    # artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='title', null=True, blank=True)
    artists = models.ManyToManyField('Artist', related_name='albums', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.artist_name

