from django.http import HttpResponse


# primera vista

def hola(request):
    return HttpResponse('Hola a todos')
    #  despues se crea la url en urls 
# otra vista
def adios(request):
    return HttpResponse('adios a todos, gracias por venir')