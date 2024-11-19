from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('pokemon/<int:number>/', views.pokemon_detail, name='pokemon_detail'),
    path('api/upload-pokemon/', views.upload_pokemon_data, name='upload_pokemon_data'),
]