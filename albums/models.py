from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField('Artist', related_name='albums', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name