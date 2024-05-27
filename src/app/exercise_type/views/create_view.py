from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.exercise_type.form import ExerciseTypeForm
from app.exercise_type.model import ExerciseType

class ExerciseTypeCreateView(CreateView):
    model = ExerciseType
    template_name = 'create.html'
    form_class = ExerciseTypeForm
    success_url = reverse_lazy('list')