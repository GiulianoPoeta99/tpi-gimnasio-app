from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.exercise.form import ExerciseForm
from app.exercise.model import Exercise

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'create.html'
    form_class = ExerciseForm
    success_url = reverse_lazy('list')