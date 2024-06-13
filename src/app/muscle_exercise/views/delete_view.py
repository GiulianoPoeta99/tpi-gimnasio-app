from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseDeleteView(DeleteView):
    model = MuscleExercise
    template_name = 'muscle_exercise/delete.html'
    success_url = reverse_lazy('muscle_exercise_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Musculos'
        context['description'] = 'Eliminar un musculo específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Musculos', 'url': 'muscle_exercise_list'},
            {'name': 'Eliminar'}
        ]
        return context