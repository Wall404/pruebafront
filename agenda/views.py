import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required

from django.db import connections

from .forms import AgregarForm, modificarItem
from .models import Contenido, Departamentos, Carreras, Materias


def home(request):
    return render(request, 'home.html')

def lista():
    api_data = getAll()

    for x in api_data:
        materia = Materias.objects.get(id_materia=x['MateriaId'])
        carrera = Carreras.objects.get(id=materia.propuesta_codigo_id_id)
        departamento = Departamentos.objects.get(id=carrera.id_departamento_id_id)

        datos = {
            'Id': x['Id'],
            'Departamento': departamento,
            'Carrera': carrera,
            'Materia': materia,
            'MateriaId': materia.id_materia,
            'Descripcion': x['Descripcion'],
        }

        print(datos)
    return datos


@login_required
def agenda_lista(request, template_name='agenda_lista.html'):
    # el nombre de la variable (datos) tiene que ser el mismo que se
    # itera en el codigo html (agenda_lista_parcial.html)

    datos = lista()

    return render(request, template_name, {'datos': datos})


def agregarItem(request):
    data = dict()

    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True

            objeto = Materias.objects.get(id = form.data['Materia'])
            formulario = {
                'MateriaId': objeto.id_materia,
                'Descripcion': form.data['Descripcion'],
                'CreatedBy': request.user.username
            }

            requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Add', json=formulario)
            
            datos = getAll()

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html', {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = AgregarForm()

    data['html_form'] = render_to_string('agregar_item_parcial.html', {'form': form}, request=request)
    return JsonResponse(data)


def Editar(request, pk):
    data = dict()
    item = getObj(pk)
    print(item)
    objeto = Materias.objects.get(id_materia=item['MateriaId'])

    if request.method == 'POST':
        form = modificarItem(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True

            datos = {
                'Id': pk,
                'MateriaId': item['MateriaId'],
                'Descripcion': form.data['Descripcion'],
                'ChangedBy': request.user.username,
            }
            print(datos)

            requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/EditBy', json=datos)

            datos = getAll()

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                         {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = modificarItem(initial= {
            'MateriaId': item['MateriaId'],
            'Nombre': objeto.nombre,
            'Descripcion': item['Descripcion']})
        form.Id = pk
        print("form: ")
        print(form.data)

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

        dato = {
            'Id': pk,
            'deletedBy': request.user.username,
        }

        requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/DeleteBy', json = dato)

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
        print(form.data)
        if form.is_valid():
            data['form_is_valid'] = True

            # requests.post(
            #     'http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SearchOne',
            #     params = form.data['Id'],
            #     headers={'Content-Type': 'application/json; charset=utf-8'}
            # )

            item = getObj(form.data['Id'])

            data['html_agenda_lista'] = render_to_string('agenda_lista_parcial.html',
                                                         {'item': item})
        else:
            data['form_is_valid'] = False
    else:
        form = buscarItem()

    data['html_form'] = render_to_string('buscar_item_parcial.html', {
        'form': form}, request=request)
    return JsonResponse(data)


def getObj(pk):
    dato = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SelectOne", params={'Id': pk}).text)
    return dato


def getAll():
    datos = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)
    return datos
