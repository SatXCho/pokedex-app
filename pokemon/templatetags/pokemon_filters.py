# pokemon/templatetags/pokemon_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def divide(value, arg):
    return value / arg

@register.filter
def index(sequence, position):
    return sequence[position]

@register.filter
def get_evolution_line(pokemon):
    evolution_line = []
    
    # Find first evolution
    current = pokemon
    while current.evolves_from:
        current = current.evolves_from
    
    # Add entire evolution line
    evolution_line.append(current)
    while current.direct_evolves_to.exists():
        current = current.direct_evolves_to.first()
        evolution_line.append(current)
        
    return evolution_line