"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jugador/<int:jugador_id>/', Login.views.info_jugadores, name='info_jugadores'),
    path('jugador/crear/', Login.views.create_jugador, name='create_jugador'),
    path('jugadores/', Login.views.jugador_list, name='jugador_list'),
    path('jugador/editar/<int:jugador_id>/', Login.views.edit_jugador, name='edit_jugador'),
    path('jugador/eliminar/<int:jugador_id>/', Login.views.delete_jugador, name='delete_jugador'),
]
