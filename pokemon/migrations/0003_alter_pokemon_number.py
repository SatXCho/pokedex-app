# Generated by Django 5.1.3 on 2024-12-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_remove_pokemon_evolution_level_pokemon_dex_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='number',
            field=models.IntegerField(),
        ),
    ]