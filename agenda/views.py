from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Agenda
from .forms import AgregarForm

import json
import requests


def home(request):
    return render(request, 'home.html')


def agenda_lista(request, template_name='agenda_lista.html'):

    response = requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select")

    # se toma lo recibido en la respuesta (response)
    # y se convierte en objeto de python
    # el nombre de la variable (datos) tiene que ser el mismo que se
    # itera en el codigo html (agenda_lista_parcial.html)
    datos = json.loads(response.text)

    return render(request, template_name, {'datos': datos})


def agregar_item(request):
    data = dict()

    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True

            requests.post(
                'http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Add',
                json.dumps(form.data),
                headers={'Content-Type': 'application/json'}
            )

            datos = json.loads(requests.get(
                "http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                        {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = AgregarForm()

    data['html_form'] = render_to_string(
        'agregar_item_parcial.html',
        {'form': form},
        request=request,
    )
    return JsonResponse(data)


def modificarItem(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True

            request.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/EditBy', 
                        json.dumps(form.data), 
                        headers={'Content-Type': 'application/json'})

            datos = json.loads(requests.get(
                "http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                        {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = AgregarForm()

    data['html_form'] = render_to_string(
        'modificar_item_parcial.html', 
        {'form':form}, 
        request=request)

    return JsonResponse(data)

# def crearItem(request):
#     if request.method == 'POST':
#         form = AgregarForm(request.POST)
#     else:
#         form = AgregarForm()
#     return modificarItem(request, form, 'agregar_item_parcial.html')

# def actualizarItem(request, pk):
#     item = get_object_or_404(Agenda, pk=pk)
#     if request.method == 'POST':
#         form = AgregarForm(request.POST, instance=item)
#     else:
#         form = AgregarForm()
#     return modificarItem(request, form, 'modificar_item_parcial.html')


def borrarItem(request, pk):
    elemento = get_object_or_404(Agenda, pk = pk)
    data = dict()
    if(request.method == 'POST'):
        elemento.delete()
        data['form_is_valid'] = True
        
        elemento = request.POST.get(
                                    'http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/DeleteBy',
                                    json.dumps(pk),
                                    headers={'Content-Type': 'null'}
                                )

        elemento = json.loads(requests.get(
            "http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)
        data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                        {'elemento': elemento})
    else:
        # elemento = json.loads(requests.get(
        #     "http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)

        # elemento = AgregarForm()
        context = {'elemento': elemento}
        data['html_form'] = render_to_string('borrar_parcial.html',
                                            context,
                                            request=request,
                                            )
    return JsonResponse(data)
