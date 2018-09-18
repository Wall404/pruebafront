from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import Agenda

import io
import json
import requests

class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

def home(request):
    return render(request, 'home.html')

def agenda_lista(request, template_name='agenda_lista.html'):
# https://github.com/swagger-api/swagger-codegen/blob/master/samples/client/petstore/python/petstore_api/rest.py

    response = requests.get("http://spc-api.unpaz.edu.ar/swagger/ui/index#!/ContenidoMinimoService/ContenidoMinimoService_SelectAll")

    r = RESTRsponse(r)
    # data = dict(response)

    # y = response.json()

    # agenda = Agenda.objects.all()

    # data['list'] = render_to_string(template_name, request)    

    return render(request, template_name)