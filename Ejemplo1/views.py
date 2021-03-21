from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 


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

# USAMOS LISTAS
"""-------------------------------------------- """

# Creamos una clase
class Profesor(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

def buenas(request):
    # recuperamos de la clase creada
    teacher= Profesor ('Amanda','Ribeiro')
    # funcion fecha actual
    fecha = datetime.datetime.now() 
    # creamos una lista
    rasgos_teacher=['pelo','ojos','boca']
    #  creamos lista vacia
    vacia_teacher=[]

    pag_vista=open('C:/Users/viaje/Desktop/pildora/Ejemplo1/Ejemplo1/plantilla/buenas.html')
    
    prof = Template(pag_vista.read())
    
    pag_vista.close()

    # pasamos por el contexto la variable asignada
    recuperar = Context({'fecha':fecha,
    'name_teacher':teacher.name,'lastname_teacher':teacher.lastname,
    'lista':['plantillas','temas','formularios'],'rasgos':rasgos_teacher, 'vacia':vacia_teacher})

    datos = prof.render(recuperar)

    return HttpResponse(datos)
    #  despues se crea la url en urls 

    # USAMOS CARGADOR LOADER con el metodo GET_TEMPLATE
"""-------------------------------------------- """

# Creamos una clase
class Chicas(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

def chicas(request):
    # recuperamos de la clase creada
    alumna= Chicas ('Amanda','Ribeiro')
    # funcion fecha actual
    fecha = datetime.datetime.now() 
    # creamos una lista
    chica_tipo=['pelo','ojos','boca']

    # utilizamos el el cargador lodade , con el metodo get.template
    pag_chicas = loader.get_template('chicas.html')

    datos ={
            'fecha':fecha,
            'name_alumna':alumna.name,
            'lastname_alumna':alumna.lastname,
            'tipo_chica':chica_tipo
        }
    # cuando se renderiza se mete directamente un dicionario , directamente o definido antes
    documento = pag_chicas.render(datos)
    
    return HttpResponse(documento)
