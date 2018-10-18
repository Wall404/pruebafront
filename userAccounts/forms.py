from django import forms
from userAccounts.models import Usuario

class login(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ()