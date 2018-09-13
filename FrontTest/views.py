from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Prueba
from django.forms import ModelForm
from collections import namedtuple

import json
import requests

# Create your views here.
# class TodoForm(ModelForm):
#     model = Prueba
    
def todo_list(request, template_name='todo_list.html'):
    data = dict()
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    y = response.json()

    context = {
        'userId': y["userId"],
        'id_todo': y["id"],
        'title': y["title"],
        'completed': y["completed"]
    }

    data['list'] = render_to_string(template_name, context, request)    