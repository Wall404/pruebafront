from django.db import models

# Create your models here.
class Agenda(models.Model):
    Id: models.IntegerField()
    Descripcion: models.CharField()
    MateriaId: models.IntegerField()
    CreatedOn: models.DateTimeField()
    CreatedBy: models.CharField()
    ChangedOn: models.DateTimeField()
    ChangedBy: models.CharField()
    DeletedOn: models.DateTimeField()
    DeletedBy: models.CharField()
    IsDeleted: models.BooleanField()