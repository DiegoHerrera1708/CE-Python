from django.contrib import admin


from Login.models import Jugador
from Login.models import Equipo

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Jugador)