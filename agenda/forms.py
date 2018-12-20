from django import forms
from .models import Departamentos, Carreras, Materias, Contenido

class AgregarForm(forms.ModelForm):
    class Meta:
        model = Contenido 
        fields= ('Departamento', 'Carrera', 'Materia')
    Descripcion = forms.CharField(widget = forms.Textarea())

class buscarItem(forms.Form):
    Id = forms.IntegerField()

class modificarItem(forms.Form):
    Descripcion = forms.CharField(widget = forms.Textarea())