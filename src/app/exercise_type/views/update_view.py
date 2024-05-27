from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.exercise_type.form import ExerciseTypeForm
from app.exercise_type.model import ExerciseType

class ExerciseTypeUpdateView(UpdateView):
    model = ExerciseType
    template_name = 'update.html'
    form_class = ExerciseTypeForm
    success_url = reverse_lazy('list')