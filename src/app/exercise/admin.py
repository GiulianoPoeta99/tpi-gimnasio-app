from django.contrib import admin
from .model import Exercise

class ExerciseAdmin (admin.ModelAdmin):
    list_display = ('name', 'display_exercise_type', 'difficulty_level', 'user')
    list_filter = ('name', 'difficulty_level', 'exercise_type')
    search_fields = ('name', 'exercise_type')
    raw_id_fields = ('difficulty_level', 'exercise_type')

    def display_exercise_type(self, obj):
        return ', '.join([exercise_type.name for exercise_type in obj.exercise_type.all()])
    
    display_exercise_type.short_description = 'Tipos de ejercicio'

admin.site.register(Exercise, ExerciseAdmin)
