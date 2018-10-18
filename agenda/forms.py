from django import forms


class AgregarForm(forms.Form):
    MateriaId = forms.IntegerField()
    Descripcion = forms.CharField()
    # CreatedOn = forms.DateTimeField()
    # CreatedBy = forms.CharField()

class buscarItem(forms.Form):
    Id = forms.IntegerField()

class modificarItem(forms.Form):
    # MateriaId = forms.IntegerField()
    Descripcion = forms.CharField()