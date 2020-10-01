""" User admin classes """

# Django
from django.contrib import admin

# Models
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
