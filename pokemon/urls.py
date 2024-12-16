from django.urls import path
from . import views
from .views import delete_team_view, edit_team_view

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('pokemon/<int:pkid>/', views.pokemon_detail, name='pokemon_detail'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/new/', views.team_create, name='team_create'),
    path('team/<int:pk>/delete/', delete_team_view, name='delete_team'),
]
