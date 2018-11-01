from django import forms

class AgregarForm(forms.Form):
    MateriaId = forms.IntegerField()
    Descripcion = forms.CharField()

class buscarItem(forms.Form):
    Id = forms.IntegerField()

class modificarItem(forms.Form):
    Descripcion = forms.CharField()