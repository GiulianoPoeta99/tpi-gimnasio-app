from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseDeleteView(DeleteView):
    model = MuscleExercise
    template_name = 'delete.html'
    success_url = reverse_lazy('list')