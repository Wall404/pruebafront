import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Agenda
from .forms import *


def home(request):
    return render(request, 'home.html')


def agenda_lista(request, template_name='agenda_lista.html'):

    # el nombre de la variable (datos) tiene que ser el mismo que se
    # itera en el codigo html (agenda_lista_parcial.html)
    
    datos = getAll()

    return render(request, template_name, {'datos': datos})


def agregarItem(request):
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

            datos = getAll()

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html', {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = AgregarForm()

    data['html_form'] = render_to_string('agregar_item_parcial.html',{'form': form},request=request)
    return JsonResponse(data)


def Editar(request, pk):
    data = dict()
    item = getObj(pk)

    if request.method == 'POST':
        form = modificarItem(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
        
            datos = {
                'Id':pk, 
                # 'MateriaId': getObj(pk)['MateriaId'],
                'MateriaId': form.data['MateriaId'],
                'Descripcion':form.data['Descripcion']
                'CreatedBy': item.CreatedBy
                }
            print(datos)

            requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/EditBy', 
                        # json.dumps(datos)
                        json = datos, 
                        # # data = {'Descripcion': form.data['Descripcion']},
                        # headers={'Content-Type': 'application/json'}
                        )

            datos = getAll()

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                         {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = modificarItem()
    form.Id = pk
    print(form.Id)
        
    data['html_form'] = render_to_string(
        'modificar_item_parcial.html',
        {'form': form},
        request=request)

    return JsonResponse(data)


def borrarItem(request, pk):
    item = getObj(pk)
    print(item)
    data = dict()

    if request.method == 'POST':
        
        data['form_is_valid'] = True
        
        requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/DeleteBy', params = {'Id':pk})

        datos = getAll()

        data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html', {'datos': datos})
    else:
        context = {'item': item}
        data['html_form'] = render_to_string('borrar_parcial.html',
                                             context,
                                             request=request
                                            )
    return JsonResponse(data)

def buscar(request):
    data = dict()
 
    if request.method == 'POST':
        form = buscarItem(request.POST)
        print(form)
        if form.is_valid():
            data['form_is_valid'] = True

            requests.post(
                'http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SearchOne',
                data=form.data,
                headers={'Content-Type': 'application/json; charset=utf-8'}
            )

            datos = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SelectOne", params = form.data).text)

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                         {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = buscarItem()

    data['html_form'] = render_to_string('buscar_item_parcial.html', {
                                         'form': form}, request=request)
    return JsonResponse(data)

def getObj(pk):
    dato = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SelectOne", params = {'Id':pk}).text)
    return dato

def getAll():
    datos = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)
    return datos
