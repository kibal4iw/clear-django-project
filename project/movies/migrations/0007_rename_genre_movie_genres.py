# Generated by Django 3.2.4 on 2021-07-03 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_rename_ganre_movie_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
    ]
