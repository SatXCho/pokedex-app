# Generated by Django 5.1.3 on 2024-12-15 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=20)),
                ('type2', models.CharField(blank=True, max_length=20, null=True)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('gender_ratio_male', models.FloatField(blank=True, null=True)),
                ('gender_ratio_female', models.FloatField(blank=True, null=True)),
                ('primary_ability', models.CharField(max_length=100)),
                ('primary_ability_description', models.TextField()),
                ('secondary_ability', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_ability_description', models.TextField(blank=True, null=True)),
                ('hidden_ability', models.CharField(blank=True, max_length=100, null=True)),
                ('hidden_ability_description', models.TextField(blank=True, null=True)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_attack', models.IntegerField()),
                ('sp_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('base_exp', models.IntegerField(default=0)),
                ('catch_rate', models.IntegerField()),
                ('egg_groups', models.CharField(blank=True, max_length=100, null=True)),
                ('base_happiness', models.IntegerField()),
                ('generation', models.CharField(max_length=50)),
                ('evolution_level', models.IntegerField(blank=True, null=True)),
                ('evolution_method', models.CharField(blank=True, max_length=100, null=True)),
                ('image_url', models.URLField(default='')),
                ('evolves_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='direct_evolves_to', to='pokemon.pokemon')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
