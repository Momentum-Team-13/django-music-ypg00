# Generated by Django 4.0.5 on 2022-07-05 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_rename_name_artist_artist_name_album_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='artists',
        ),
    ]
