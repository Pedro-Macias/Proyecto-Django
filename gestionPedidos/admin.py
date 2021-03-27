from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos,Pedidos


# crear una clase para mostrar lo que queremos de cada Modelo
class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','phone','direccion')
    # busqueda
    search_fields=('nombre','direccion')

class ArticulosAdmin(admin.ModelAdmin):
    # crear un filtro 
    list_filter=('seccion',)


class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    # filtro por fecha
    list_filter=('fecha',)
    # filtro migas de pan
    date_hierarchy='fecha'

# Register your models here.



admin.site.register(Clientes, ClientesAdmin)

admin.site.register(Articulos,ArticulosAdmin)

admin.site.register(Pedidos, PedidosAdmin)