from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
# class Agenda(models.Model):
#     # Id: models.IntegerField()
#     Descripcion = models.CharField(max_length=255)
#     MateriaId = models.IntegerField()
#     CreatedOn = models.DateTimeField()
#     CreatedBy = models.CharField(max_length=255)
#     ChangedOn = models.DateTimeField()
#     ChangedBy = models.CharField(max_length=255)
#     DeletedOn = models.DateTimeField()
#     DeletedBy = models.CharField(max_length=255)
#     IsDeleted = models.BooleanField()

class Departamentos(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Carreras(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    nombre_propuesta = models.CharField(max_length=255)
    id_departamento_id = models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_propuesta

class Materias(models.Model):
    id_materia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    propuesta_codigo_id = models.ForeignKey(Carreras, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Contenido(models.Model):
    Departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    Carrera = ChainedForeignKey (
        Carreras,
        chained_field="Departamento",
        chained_model_field='id_departamento_id',
    )
    Materia = ChainedForeignKey (
        Materias,
        chained_field="Carrera",
        chained_model_field="propuesta_codigo_id",
    )