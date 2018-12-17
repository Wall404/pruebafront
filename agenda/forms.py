from django import forms
from .models import Departamentos, Carreras, Materias, Contenido

class AgregarForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(AgregarForm, self).__init__(*args, **kwargs)
    #     self.fields['Departamento'].choices = list(Departamentos.objects.values_list('id', 'nombre'))
    #     self.fields['Carrera'].choices = list(Carreras.objects.values_list('id', 'nombre_propuesta'))
    #     self.fields['Materia'].choices = list(Materias.objects.values_list('id', 'nombre'))

    class Meta:
        model = Contenido 
        fields= ('Departamento', 'Carrera', 'Materia')
    Descripcion = forms.CharField(widget = forms.Textarea())

class buscarItem(forms.Form):
    Id = forms.IntegerField()

class modificarItem(forms.Form):
    Descripcion = forms.CharField(widget = forms.Textarea())