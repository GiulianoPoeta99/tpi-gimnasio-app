from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.exercise.model import Exercise

class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'delete.html'
    success_url = reverse_lazy('list')