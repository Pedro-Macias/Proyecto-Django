from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
# importar la clase forms
from gestionPedidos.forms import Form_Contacto

# Create your views here.

def busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def buscar(request):

    if request.GET['producto']:
        # mensaje = 'articulo buscado: %s'%request.GET['producto']
        prd =request.GET['producto']
        # limitar la busqueda
        if len(prd)>20:
            mensaje = 'texto demasiado largo'
        else:
            # icontains sustituye al likes de sql
            # SELECT * Articulos LIKE nombre="prd"
            articulos = Articulos.objects.filter(nombre__icontains=prd)

            # rederigir al html que queremos 
            return render(request,'resultado_busqueda.html',{'articulos':articulos, 'query':prd})
    else:
        mensaje = 'no introduciste nada'  
    
    return HttpResponse(mensaje)


# FORMULARIO DE CONTACTO
'''
def contacto(request):
    if request.method == 'POST':
        # enviar correo electronico
        mail_asunto=request.POST['asunto']
        mail_texto = request.POST['mensaje'] + ' ' + request.POST['email']
        mail_from = settings.EMAIL_HOST_USER
        # mail de quien recibe 
        mail_recibir = ['pin@pin.com']

        send_mail(mail_asunto,mail_texto,mail_from,mail_recibir)
        # mensaje de gracias
        return render(request,'gracias.html')
    
    return render (request,'contacto.html')
'''
def contacto(request):
    if request.method=='POST':
        miFormulario = Form_Contacto(request.POST)
        if miFormulario.is_valid():
            inf_Formulario = miFormulario.cleaned_data
            send_mail (inf_Formulario['asunto'],inf_Formulario['mensaje'],
            inf_Formulario.get('email',''),['pin@pin.com'])

            return render(request,'gracias.html')
    
    else:
        miFormulario=Form_Contacto()
    
    return render(request,'formulario_contacto.html',{'form':miFormulario})
