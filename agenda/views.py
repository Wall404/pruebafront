from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Agenda
from .forms import Agregar_item

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

def agregar_item(request):
    data = dict()

    if request.method == 'POST':
        form = Agregar_item(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            agenda = Agenda.objects.all()
            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial',
            { 'agenda': agenda })
        else:
            data['form_is_valid'] = False
    else:
        form = Agregar_item()

    form = Agregar_item()
    ctx = {'form':form}
    data['html_form'] = render_to_string('agenda/includes/agregar_item_parcial.html',
        ctx,
        request=request,
    )

    return JsonResponse(data)