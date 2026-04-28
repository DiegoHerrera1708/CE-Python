from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'posicion', 'equipo']
        labels = {
            'nombre': 'Nombre del Jugador',
            'posicion': 'Posición',
            'equipo': 'Equipo al que Pertenece',
        }
        