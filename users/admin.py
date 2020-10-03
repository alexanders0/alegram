""" User admin classes """

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    # Mostrar datos de cada usuario al listar la app en el Admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Establecer datos como links
    list_display_links = ('pk', 'user')
    # Permitir editar datos sin entrar al registro
    list_editable = ('phone_number', 'website', 'picture')
    # Buscar por campos
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # Agregar filtros (el orden importa)
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )
    # Valores a presentar por registro
    # El primer valor de la tupla es la seccion
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    # Valores que no se pueden modificar
    readonly_fields = ('created', 'modified')


# El siguiente codigo permite crear un usuario con los datos del modelo
class ProfileInline(admin.StackedInline):
    """ Profile in-line admin por users """

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Adds profile admin to base user admin """

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
