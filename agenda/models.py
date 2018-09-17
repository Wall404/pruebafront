from django.db import models


# Create your models here.
class Agenda(models.Model):
    Id: models.IntegerField()
    Descripcion: models.CharField(max_length=200)
    MateriaId: models.IntegerField()
    CreatedOn: models.DateTimeField()
    CreatedBy: models.CharField(max_length=200)
    ChangeOn: models.DateTimeField()
    ChangedBy: models.CharField(max_length=200)
    DeletedOn: models.DateTimeField()
    DeletedBy: models.CharField(max_length=200)
    IsDeleted: bool

    # def __str__(self):
    #     return self.user_ID
