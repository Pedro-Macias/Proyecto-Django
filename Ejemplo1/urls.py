"""Ejemplo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Ejemplo1.views import hola, adios, lahora, queEdad, buenas

urlpatterns = [
    path('admin/', admin.site.urls),
    # creamos la url de la primera vista
    path('hola/',hola),
    # creamos la url de la segunda vista
    path('salimos/',adios),
    # creamos la url la vista de la hora actual
    path('hora/',lahora),
    # creamos la url la vista de la edad futura indicandole un parametro de numero entero
    path('edad/<int:year>',queEdad),
    # creamos la url la vista  buenas
    path('buenas/',buenas),

]
