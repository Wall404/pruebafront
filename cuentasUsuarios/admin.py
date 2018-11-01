from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import usuarioCustom

class usuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Información Personal'), {'fields': ('first_name', 'last_name')}),
        # (('Roles'), ('role'))
        (('Permisos'), {'fields': ('is_admin', 'is_docente', 'is_dir_carrera',
                                        'is_departamento', 'is_dir_prog_curricular',
                                        'is_academica_admin', 'is_academica')}),
                                    #    'groups', 'user_permissions')}),
        # (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = usuarioCustom
    list_display = ['email', 'username', 'first_name', 'last_name']
    list_select_related = True
    list_display_links = ('username',) #link field
    ordering = ('username', 'last_name')
    search_fields = ('email', 'username')

admin.site.unregister(Group) #Remueve las directivas de grupo
admin.site.register(usuarioCustom, usuarioAdmin) #registra el usuario personalizado