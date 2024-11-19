# pokemon/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Pokemon

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, number):
    pokemon = get_object_or_404(Pokemon, number=number)
    return render(request, 'pokemon/pokemon_detail.html', {'pokemon': pokemon})

@csrf_exempt
def upload_pokemon_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            for pokemon_data in data:
                pokemon_id = int(pokemon_data["id"])
                
                pokemon, created = Pokemon.objects.update_or_create(
                    number=pokemon_id,
                    defaults={
                        "name": pokemon_data["name"],
                        "description": pokemon_data["description"],
                        "type1": pokemon_data["type"][0],
                        "type2": pokemon_data["type"][1] if len(pokemon_data["type"]) > 1 else None,
                        "height": float(pokemon_data["height"].split("m")[0].strip("() ")),
                        "weight": float(pokemon_data["weight"].split("kg")[0].strip("() ")),
                        "abilities": ", ".join(pokemon_data["abilities"]),
                        "hp": pokemon_data["stats"]["hp"],
                        "attack": pokemon_data["stats"]["attack"],
                        "defense": pokemon_data["stats"]["defense"],
                        "sp_attack": pokemon_data["stats"]["sp.atk"],
                        "sp_defense": pokemon_data["stats"]["sp.def"],
                        "speed": pokemon_data["stats"]["speed"],
                        "image_url": pokemon_data["sprites"]
                    }
                )

            return JsonResponse({"status": "success", "message": f"Imported {len(data)} Pokemon"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Only POST requests allowed"}, status=405)