from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from cuentasUsuarios.models import usuarioCustom

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = usuarioCustom
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = usuarioCustom
        fields = ('email','username')