# Generated by Django 4.0.6 on 2022-07-05 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0015_remove_album_artists_album_artists_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artists',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='albums',
            new_name='album',
        ),
    ]
