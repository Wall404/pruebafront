"""pruebafront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from django.contrib.auth import views as auth_views

from agenda import views as agenda_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # path('users/', include('pruebafront.urls')),

    path('users/', include('django.contrib.auth.urls')),

    url('^', include('django.contrib.auth.urls')),

    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),

    path('', agenda_views.home, name='home'),

    path('agenda_lista/', agenda_views.agenda_lista, name='agenda_lista'),

    path('agenda_lista/agregar_item/', agenda_views.agregarItem, name='agregar_item'),

    url(r'^(?P<pk>\d+)/borrar/$', agenda_views.borrarItem, name='borrar_item'),

    url(r'^(?P<pk>\d+)/editar/$', agenda_views.Editar, name='editar'),

    path('agenda_lista/buscar_item/', agenda_views.buscar, name='buscar_item'),
]
