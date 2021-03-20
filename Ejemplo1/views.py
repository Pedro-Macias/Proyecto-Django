from django.http import HttpResponse
import datetime
from django.template import Template, Context


# utilizando clases
class Persona(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname




def hola(request):
    # recuperamos de la clase creada
    profesor= Persona ('Juan','Diaz')

    # cremaos una variable
    name ='Pedro'
    lastname ='Macias'
    
    ahora = datetime.datetime.now()
    
    pag_externa=open('C:/Users/viaje/Desktop/pildora/Ejemplo1/Ejemplo1/plantilla/hola.html')
    
    plt = Template(pag_externa.read())
    
    pag_externa.close()

    # pasamos por el contexto la variable asignada
    ctx = Context({'name_pax':name,'lastname_pax':lastname,'fecha':ahora,
    'name_pro':profesor.name,'lastname_pro':profesor.lastname})

    pagina = plt.render(ctx)

    return HttpResponse(pagina)
    #  despues se crea la url en urls 
# otra vista
def adios(request):
    return HttpResponse('adios a todos, gracias por venir')


# mostrar contenido dinamico

def lahora(request):
    fecha_actual = datetime.datetime.now()
    # poner algo de estilo html
    paginahora= """
    <html>
    <body>
    <h2>
    fecha y hora actual %s
    </h2>
    </body>
    <html>
    """ % fecha_actual

    return HttpResponse(paginahora)

# que edad tendremos en un año
def queEdad(request,year):
    
    edadActual = 18
    tiempo = year -2021
    edadFutura = edadActual + tiempo
    paginaEdad= """
    <html>
    <body>
    <h2>
    en el año  %s tendra %s años
    </h2>
    </body>
    <html>
    """ %(year,edadFutura)

    return HttpResponse(paginaEdad)
