from django.shortcuts import redirect, render
from .models import Equipo, Jugador
from .forms import JugadorForm
# Create your views here.

def info_jugadores(request, jugador_id):
    jugador = Jugador.objects.get(pk=jugador_id)
    return render(request, 'info.html', {'jugador': jugador})

def create_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
    else:
        form = JugadorForm()
    return render(request, 'create_jugador.html', {'form': form})

def jugador_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugador_list.html', {'jugadores': jugadores})

def edit_jugador(request, jugador_id):
    jugador = Jugador.objects.get(pk=jugador_id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'editar_jugador.html', {'form': form})

def delete_jugador(request, jugador_id):
    jugador = Jugador.objects.get(pk=jugador_id)
    jugador.delete()
    return redirect('jugador_list')