from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.muscle_exercise.form import MuscleExerciseForm
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseCreateView(CreateView):
    model = MuscleExercise
    template_name = 'create.html'
    form_class = MuscleExerciseForm
    success_url = reverse_lazy