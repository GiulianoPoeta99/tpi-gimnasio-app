from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.exercise.form import ExerciseForm 
from app.exercise.model import Exercise

class ExerciseUpdateView(UpdateView):
    model = Exercise
    template_name = 'update.html'
    form_class = ExerciseForm
    success_url = reverse_lazy('list')