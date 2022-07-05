# Generated by Django 4.0.5 on 2022-07-05 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_delete_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('albums', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_name', to='albums.album')),
            ],
        ),
    ]
