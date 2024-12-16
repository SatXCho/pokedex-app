from django import forms
from .models import Team, Pokemon

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'pokemon1', 'pokemon2', 'pokemon3', 'pokemon4', 'pokemon5', 'pokemon6']
        widgets = {
            'pokemon1': forms.Select,
            'pokemon2': forms.Select,
            'pokemon3': forms.Select,
            'pokemon4': forms.Select,
            'pokemon5': forms.Select,
            'pokemon6': forms.Select,
        }