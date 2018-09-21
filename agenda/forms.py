from django import forms
from .models import Agenda

class Agregar_item(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = (
            # 'Id', 
            # 'Descripcion',
            # 'MateriaId',
            # 'CreatedOn',
            # 'CreatedBy',
            # 'ChangedOn',
            # 'ChangedBy',
            # 'DeletedOn',
            # 'Deletedby',
            # 'IsDeleted',
        )