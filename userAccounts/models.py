from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    nombre = models.CharField()
    apellido = models.CharField()
    creadoEn = models.DateTimeField(auto_now_add=True)
    