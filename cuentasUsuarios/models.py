from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class usuarioCustom(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)
    is_dir_carrera = models.BooleanField(default=False)
    is_departamento = models.BooleanField(default=False)
    is_dir_prog_curricular = models.BooleanField(default=False)
    is_academica_admin = models.BooleanField(default=False)
    is_academica = models.BooleanField(default=False)

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    createdOn = models.DateTimeField(auto_now_add=True)


    # DOCENTE = 1
    # DIRECTOR_CARRERA = 2
    # DEPARTAMENTO = 3
    # DIR_PROG_CURRICULAR = 4
    # ACADEMICA_ADMIN = 5
    # ACADEMICA = 6
    # ADMIN = 7

    # ROLE_CHOICES = (
    #     (DOCENTE, 'Docente'),
    #     (DIRECTOR_CARRERA, 'Director de Carrera'),
    #     (DEPARTAMENTO, 'Departamento'),
    #     (DIR_PROG_CURRICULAR, 'Direccion de Programas Curricular'),
    #     (ACADEMICA_ADMIN, 'Academica Admin'),
    #     (ACADEMICA, 'Academica'),
    #     (ADMIN, 'Admin'),
    # )
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)

class usuarioAdmin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)

class usuarioDocente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)
    
class usuarioDirectorCarrera(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)
    
class usuarioDepartament(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)
    
class usuarioDirProgCurricular(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)
    
class usuarioAcademicaAdmin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)
    
class usuarioAcademica(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    changedOn = models.DateTimeField(null=True)