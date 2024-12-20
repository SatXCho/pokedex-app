from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    csvid = models.IntegerField(default=-1)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    dex_entry = models.TextField(default='pokemons dae')
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20, null=True, blank=True)
    height = models.FloatField()  # in meters
    weight = models.FloatField()  # in kg
    gender_ratio_male = models.FloatField(null=True, blank=True)
    gender_ratio_female = models.FloatField(null=True, blank=True)
    primary_ability = models.CharField(max_length=100)
    primary_ability_description = models.TextField()
    secondary_ability = models.CharField(max_length=100, null=True, blank=True)
    secondary_ability_description = models.TextField(null=True, blank=True)
    hidden_ability = models.CharField(max_length=100, null=True, blank=True)
    hidden_ability_description = models.TextField(null=True, blank=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField() 
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    base_exp = models.IntegerField(default=0)
    catch_rate = models.IntegerField()
    egg_groups = models.CharField(max_length=100, null=True, blank=True)
    base_happiness = models.IntegerField()
    generation = models.CharField(max_length=50)
    evolves_from = models.ForeignKey('self', null=True, blank=True, 
                                   on_delete=models.SET_NULL,
                                   related_name='direct_evolves_to')
    evolution_method = models.CharField(max_length=100, null=True, blank=True)

    def image_url(self):
        return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{self.number}.png"

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"#{self.number} {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')  # Link to the user
    pokemon1 = models.ForeignKey(Pokemon, related_name='team_slot1', on_delete=models.CASCADE)
    pokemon2 = models.ForeignKey(Pokemon, related_name='team_slot2', on_delete=models.CASCADE, null=True, blank=True)
    pokemon3 = models.ForeignKey(Pokemon, related_name='team_slot3', on_delete=models.CASCADE, null=True, blank=True)
    pokemon4 = models.ForeignKey(Pokemon, related_name='team_slot4', on_delete=models.CASCADE, null=True, blank=True)
    pokemon5 = models.ForeignKey(Pokemon, related_name='team_slot5', on_delete=models.CASCADE, null=True, blank=True)
    pokemon6 = models.ForeignKey(Pokemon, related_name='team_slot6', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Owner: {self.user.username})"
