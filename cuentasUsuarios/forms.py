from django import forms
from cuentasUsuarios.models import usuario

class login(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ()