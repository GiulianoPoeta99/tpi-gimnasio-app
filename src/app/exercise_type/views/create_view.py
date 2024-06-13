from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.exercise_type.form import ExerciseTypeForm
from app.exercise_type.model import ExerciseType

class ExerciseTypeCreateView(CreateView):
    model = ExerciseType
    template_name = 'exercise_type/create.html'
    form_class = ExerciseTypeForm
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        context['title'] = 'Tipos de Ejercicios'
        context['description'] = 'Crear un nuevo tipo de ejercicio.'
        context['breadcrum_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de ejercicio', 'url': 'exercise_type_list'},
            {'name': 'Crear'}
        ]
        return context
    
    # override
    def get_success_url(self):
        return reverse_lazy('exercise_type_detail', kwargs={'pk': self.object.pk})