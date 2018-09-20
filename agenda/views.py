from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import Agenda

import urllib3
import json
import requests

def home(request):
    return render(request, 'home.html')

def agenda_lista(request, template_name='agenda_lista.html'):

    response = requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select")
    
    # se toma lo recibido en la respuesta (response) 
    # y se convierte en objeto de python
    # el nombre de la variable (datos) tiene que ser el mismo que se
    # itera en el codigo html (agenda_lista.html)
    datos = json.loads(response.text)

    return render(request, template_name, {'datos': datos })
