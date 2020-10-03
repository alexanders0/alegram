""" Post admin classes """

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post admin. """

    list_display = ('pk', 'title', 'photo', 'user')
    list_display_links = ('pk', 'title')
    list_editable = ('photo',)
    search_fields = ('user__username', 'title')
    list_filter = ('created', 'modified')
    fieldsets = (
        ('Author', {
            'fields': (('user', 'profile'),)
        }),
        ('Details', {
            'fields': (
                ('title', 'photo')
            )
        })
    )
    readonly_fields = ('created', 'modified')
