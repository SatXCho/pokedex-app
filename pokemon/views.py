# pokemon/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from django.http import JsonResponse
from django.db.models import Exists, OuterRef, Count, F, Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Pokemon

# def explore(request):
    # query = request.GET.get('search', '').strip()
    
    # if query:
    #     books_list = Book.objects.filter(
    #         Q(title__icontains=query) | Q(author__icontains=query)
    #     )
    # else:
    #     books_list = Book.objects.all()

    # books_list = books_list.annotate(
    #     is_saved=Exists(
    #         Wishlist.objects.filter(user=request.user, book_id=OuterRef('pk'))
    #     )
    # )
    
    # paginator = Paginator(books_list, 20)
    
    # page = request.GET.get('page', 1)
    
    # try:
    #     books = paginator.page(page)
    # except PageNotAnInteger:
    #     books = paginator.page(1)
    # except EmptyPage:
    #     books = paginator.page(paginator.num_pages)
    
    # return render(request, "books/explore.html", {
    #     'books': books,  
    #     'search_query': query,
    #     'is_paginated': books.has_other_pages(),
    # })

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
