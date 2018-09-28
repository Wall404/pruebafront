from django import forms

class AgregarForm(forms.Form):
    MateriaId = forms.IntegerField()
    Descripcion = forms.CharField()
