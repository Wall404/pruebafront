from django.db import models


# Create your models here.
class Agenda(models.Model):
    Id: models.IntegerField()
    Descripcion: models.CharField(max_length=200)
    MateriaId: models.IntegerField()
    CreatedOn: models.DateTimeField(auto_now_add=True)
    CreatedBy: models.CharField(max_length=200)
    ChangeOn: models.DateTimeField()
    ChangedBy: models.CharField(max_length=200)
    DeletedOn: models.DateTimeField()
    DeletedBy: models.CharField(max_length=200)
    IsDeleted: models.BooleanField(default=False)

    # def __init__(self):
    #     return self.agenda = [
    #         'Id',
    #         'Descripcion',
    #         'MateriaId',
    #         'CreatedOn',
    #         'CreatedBy',
    #         'ChangedOn',
    #         'ChangedBy',
    #         'DeletedOn',
    #         'DeletedBy',
    #         'IsDeleted'
    #         ]

    # def query(self):
    #     url = 'http://spc-api.unpaz.edu.ar/api/ContenidoMinimo/Select/'