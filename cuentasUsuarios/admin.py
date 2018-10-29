from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# from cuentasUsuarios.models import Profile

# # Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = (
#         'username',
#         'email',
#         'first_name',
#         'last_name',
#         'get_role',
#         )
#     list_select_related = ('profile', )

#     def get_role(self, instance):
#         return instance.profile.role
#     get_role.short_description = "Rol"

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)