from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import Agenda

import json
import requests

# Create your views here.
# class TodoForm(ModelForm):
#     model = Prueba

def home(request):
    return render(request, 'home.html')

def agenda_lista(request, template_name='agenda_lista.html'):
    response = requests.get("http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select")

    data = dict(response)

    y = response.json()

    # context = {
    #     'userId': y["userId"],
    #     'id_todo': y["id"],
    #     'title': y["title"],
    #     'completed': y["completed"]
    # }

    data['list'] = render_to_string(template_name, request)    

    return render(request, template_name, context=data)