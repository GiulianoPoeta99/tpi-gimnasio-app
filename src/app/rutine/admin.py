from django.contrib import admin

from .model import Rutine

class RutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'difficulty_level', 'display_rutine_types')
    list_filter = ('user', 'difficulty_level', 'rutine_type')
    search_fields = ('name', 'user__username')
    raw_id_fields = ('user', 'difficulty_level', 'rutine_type')

    def display_rutine_types(self, obj):
        return ', '.join([rutine_type.name for rutine_type in obj.rutine_type.all()])

    display_rutine_types.short_description = 'Tipos de Rutina'

admin.site.register(Rutine, RutineAdmin)
