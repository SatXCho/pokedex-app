# Generated by Django 5.1.3 on 2024-12-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_remove_pokemon_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='csvid',
            field=models.IntegerField(default=-1, unique=True),
        ),
    ]
