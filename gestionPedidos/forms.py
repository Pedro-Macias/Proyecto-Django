# archivo para crear formularios
from django import forms

# formulario de contacto
class Form_Contacto(forms.Form):
    asunto =forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()