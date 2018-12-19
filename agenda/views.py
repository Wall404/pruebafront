import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.db import connections

from .forms import AgregarForm, modificarItem
from .models import Contenido, Departamentos, Carreras, Materias


def home(request):
    return render(request, 'home.html')

def listar():
    datos = []
    dato = {}
    api_data = getAll()

    for x in api_data:
        materia = Materias.objects.get(id=x['MateriaId'])
        carrera = Carreras.objects.get(id=materia.propuesta_codigo_id_id)
        departamento = Departamentos.objects.get(id=carrera.id_departamento_id_id)

        dato.update ({
            'Id': x['Id'],
            'Departamento': departamento.nombre,
            'Carrera': carrera.nombre_propuesta,
            'Materia': materia.nombre,
            'MateriaId': materia.id,
            'Descripcion': x['Descripcion'],
        })
        datos.append(dato.copy())

    return datos

@login_required
def lista(request, template_name='lista.html'):
    # el nombre de la variable (datos) tiene que ser el mismo que se
    # itera en el codigo html (lista_parcial.html)

    lista_datos = listar()
    
    pagina = request.GET.get('page', 1)

    paginator = Paginator(lista_datos, 10)

    print(paginator.num_pages)

    datos = paginator.page(pagina)

    return render(request, template_name, {'datos': datos})


def agregarItem(request):
    data = dict()

    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True

            objeto = Materias.objects.get(id = form.data['Materia'])
            formulario = {
                'MateriaId': objeto.id,
                'Descripcion': form.data['Descripcion'],
                'CreatedBy': request.user.username
            }

            requests.post('http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Add', json=formulario)
            
            datos = listar()

            data['html_lista'] = render_to_string('lista_parcial.html', {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = AgregarForm()

    data['html_form'] = render_to_string('agregar_item_parcial.html', {'form': form}, request=request)
    return JsonResponse(data)


def Editar(request, pk):
    data = dict()
    item = getObj(pk)
    # print(item)
    objeto = Materias.objects.get(id=item['MateriaId'])

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

            datos = listar()

            data['html_lista'] = render_to_string('lista_parcial.html',
                                                         {'datos': datos})
        else:
            data['form_is_valid'] = False
    else:
        form = modificarItem(initial= {'Descripcion': item['Descripcion']})
        form.Id = pk

    data['html_form'] = render_to_string(
        'modificar_item_parcial.html',
        {'form': form, 'item': item, 'objeto':objeto},
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

        datos = listar()

        data['html_lista'] = render_to_string('lista_parcial.html', {'datos': datos})
    else:
        context = {'item': item}
        data['html_form'] = render_to_string('borrar_parcial.html',
                                             context,
                                             request=request
                                             )
    return JsonResponse(data)


def ver(request, pk):
    item = getObj(pk)
    data = dict()

    dato = {
        'Materia' : Materias.objects.get(id=item['MateriaId']),
        'Carrera' : Carreras.objects.get(id=Materias.objects.get(id=item['MateriaId']).propuesta_codigo_id_id),
        'Departamento' : Departamentos.objects.get(id=Carreras.objects.get(id=Materias.objects.get(id=item['MateriaId']).propuesta_codigo_id_id).id_departamento_id_id),
    }

    print(dato)

    data['html_form'] = render_to_string('ver_item_parcial.html', {'item': item, 'dato':dato}, request=request)
    return JsonResponse(data)


def getObj(pk):
    dato = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/SelectOne", params={'Id': pk}).text)
    return dato


def getAll():
    datos = json.loads(requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select").text)
    return datos
