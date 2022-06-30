from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    # created_at = models.DateTimeField() # research how to autofill

    def __str__(self):
        return f'{self.title}'

class Artist(models.Model):
    name = models.CharField(max_length=255)
    # albums = models.ForeignObject()

    def __str__(self):
        return f'{self.name}'
