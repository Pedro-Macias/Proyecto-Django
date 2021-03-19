from django.http import HttpResponse
import datetime



# primera vista

def hola(request):
    # poner algo de estilo html
    pagina = """
    <html>
    <body>
    <h1>
    hola a todos
    </h1>
    </body>
    <html>
    """

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
