from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.exercise_type.model import ExerciseType

class ExerciseTypeDeleteView(DeleteView):
    model = ExerciseType
    template_name = 'delete.html'
    success_url = reverse_lazy('list')