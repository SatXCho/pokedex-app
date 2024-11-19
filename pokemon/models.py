# pokemon/models.py
from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20, null=True, blank=True)
    height = models.FloatField()  # in meters
    weight = models.FloatField()  # in kg
    gender_ratio = models.CharField(max_length=50, null=True, blank=True)
    egg_groups = models.CharField(max_length=100, null=True, blank=True)
    abilities = models.CharField(max_length=200)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    image_url = models.URLField()
    evolution_level = models.IntegerField(null=True, blank=True)
    evolution_method = models.CharField(max_length=100, null=True, blank=True)
    evolves_from = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='direct_evolves_to')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"#{self.number:03d} {self.name}"