# pokemon/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import JsonResponse, HttpResponseForbidden
from django.db.models import Exists, OuterRef, Count, F, Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Pokemon

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team
from .forms import TeamForm

@login_required
def team_list(request):
    teams = Team.objects.filter(user=request.user)  
    return render(request, 'pokemon/team_list.html', {'teams': teams})

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id, user=request.user) 
    return render(request, 'pokemon/team_detail.html', {'team': team})

@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.user = request.user 
            team.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'pokemon/team_form.html', {'form': form})

@login_required
def edit_team_view(request, pk):
    team = get_object_or_404(Team, pk=pk)

    # Ensure only the owner can edit the team
    if team.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this team.")

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', pk=team.pk)  # Redirect to the team detail page
    else:
        form = TeamForm(instance=team)

    return render(request, 'pokemon/edit_team.html', {'form': form, 'team': team})

@login_required
def delete_team_view(request, pk):
    team = get_object_or_404(Team, pk=pk)

    
    if team.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this team.")

    if request.method == 'POST':
        team.delete()
        return redirect('team_list')  

    return render(request, 'pokemon/team_confirm_delete.html', {'team': team})

@login_required
def pokemon_list(request):
    query = request.GET.get('search', '').strip()
    
    if query:
        pokemon_list = Pokemon.objects.filter(
            Q(name__icontains=query) | Q(type1__icontains=query)  | Q(type2__icontains=query)
        )
    else:
        pokemon_list = Pokemon.objects.all()

    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemon_list})

@login_required
def pokemon_detail(request, pkid):
    pokemon = get_object_or_404(Pokemon, pk=pkid)
    return render(request, 'pokemon/pokemon_detail.html', {'pokemon': pokemon})
