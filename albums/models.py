from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField() # research how to autofill

class Artist(models.Model):
    name = models.CharField(max_length=255)
    albums = models.ForeignObject()
