# Generated by Django 4.0.6 on 2022-07-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0018_remove_artist_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='albums', to='albums.artist'),
        ),
    ]