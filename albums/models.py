from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artists = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.title}'

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    albums = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='artist_name', null=True, blank=True)

    # def __str__(self):
    #     return f'{self.name}'
