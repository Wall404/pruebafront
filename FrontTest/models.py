from django.db import models


# Create your models here.
class Prueba(models.Model):
    userId: models.IntegerField()
    id_todo: models.IntegerField()
    title: models.CharField(max_length=200)
    completed: bool

    # def __str__(self):
    #     return self.user_ID
