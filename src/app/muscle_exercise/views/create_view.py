from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.muscle_exercise.form import MuscleExerciseForm
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseCreateView(CreateView):
    model = MuscleExercise
    template_name = 'muscle_exercise/create.html'
    form_class = MuscleExerciseForm
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Musculos'
        context['description'] = 'Crear un nuevo musculo.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Musculos', 'url': 'muscle_exercise_list'},
            {'name': 'Crear'}
        ]
        return context
    
    # override
    def get_success_url(self):
        return reverse_lazy('muscle_exercise_detail', kwargs={'pk': self.object.pk})