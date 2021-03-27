from django.db import models

# Create your models here.

# crear una clase por cada tabla que quieras

class Clientes (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    # solo direcciones de email validas y que no sea requerido
    email= models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=9, verbose_name='Telefono')

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

    # crear la funcion string 
    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio %s'%(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()