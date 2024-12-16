import csv
from django.core.management.base import BaseCommand

from pokemon.models import Pokemon

def get_evo(pkid):
        if pkid == "NULL":
            return None
        pokemon = Pokemon.objects.filter(csvid=pkid).first()
        print(pkid, pokemon)
        if pokemon:
            return pokemon
        return None
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs["csv_file"]

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            pokemons = []
            for row in reader:
                try:
                    pkmn = Pokemon(
                            csvid = row['\ufeffPokemon Id'],
                            number = row['Pokedex Number'],
                            name = row['Pokemon Name'][1:-1],
                            classification = row['Classification'][1:-1],
                            type1 = row['Primary Type'][1:-1],
                            type2 = row['Secondary Type'][1:-1] if row['Secondary Type']!="NULL" else None,
                            height = row['Pokemon Height'],
                            weight = row['Pokemon Weight'],
                            gender_ratio_male = row['Male Ratio'],
                            gender_ratio_female = row['Female Ratio'],
                            primary_ability = row['Primary Ability'][1:-1],
                            primary_ability_description = row['Primary Ability Description'][1:-1],
                            secondary_ability = row['Secondary Ability'][1:-1] if row['Secondary Ability']!="NULL" else None,
                            secondary_ability_description = row['Secondary Ability Description'][1:-1] if row['Secondary Ability Description']!="NULL" else None,
                            hidden_ability = row['Hidden Ability'][1:-1] if row['Hidden Ability']!="NULL" else None,
                            hidden_ability_description = row['Hidden Ability Description'][1:-1] if row['Hidden Ability Description']!="NULL" else None,
                            hp = row['Health Stat'],
                            attack = row['Attack Stat'],
                            defense = row['Defense Stat'],
                            sp_attack = row['Special Attack Stat'],
                            sp_defense = row['Special Defense Stat'],
                            speed = row['Speed Stat'],
                            base_exp = row['Experience Growth Total'],
                            catch_rate = row['Catch Rate'],
                            egg_groups = row['Primary Egg Group'][1:-1],
                            base_happiness = row['Base Happiness'],
                            generation = row['Game(s) of Origin'][1:-1],
                            evolves_from = get_evo(row['Pre-Evolution Pokemon Id']),
                            evolution_method = row['Evolution Details'][1:-1] if row['Evolution Details']!="NULL" else None,
                            dex_entry = row['Pokedex Entry']
                    )
                    pkmn.save()
                    pokemons.append(pkmn)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing pokemon {row['Pokemon Name']}: {e}"))
                    continue

            
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(pokemons)} pokemons."))