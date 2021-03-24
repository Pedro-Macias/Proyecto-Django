from django.db import models

# Create your models here.

# crear una clase por cada tabla que quieras

class Clientes (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    # solo direcciones de email validas
    email= models.EmailField()
    phone = models.CharField(max_length=9)

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()