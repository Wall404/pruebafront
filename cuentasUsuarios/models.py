from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class user(AbstractUser):
    is_docente = models.BooleanField(default=False)
    is_director_carrera = models.BooleanField(default=False)
    is_departamento = models.BooleanField(default=False)
    is_dir_prog_curricular = models.BooleanField(default=False)
    is_academica_admin = models.BooleanField(default=False)
    is_academica = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class userAdmin(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userDocente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userDirectorCarrera(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userDepartamento(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userDirProgCurricular(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userAcademicaAdmin(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

class userAcademica(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    

# class Profile(models.Model):
#     DOCENTE = 1
#     DIRECTOR_CARRERA = 2
#     DEPARTAMENTO = 3
#     DIRECCION_PROGRAMAS_CURRICULAR = 4
#     ACADEMICA_ADMIN = 5
#     ACADEMICA = 6
#     ADMIN = 7

#     ROLE_CHOICES = (
#         (DOCENTE, 'Docente'),
#         (DIRECTOR_CARRERA, 'Director de Carrera'),
#         (DEPARTAMENTO, 'Departamento'),
#         (DIRECCION_PROGRAMAS_CURRICULAR, 'Direccion de Programas Curricular'),
#         (ACADEMICA_ADMIN, 'Academica Admin'),
#         (ACADEMICA, 'Academica'),
#         (ADMIN, 'Admin'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

#     @receiver(post_save, sender=User)
#     def create_or_update_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#         instance.profile.save()