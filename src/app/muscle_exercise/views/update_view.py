from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.muscle_exercise.form import MuscleExerciseForm
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseUpdateView(UpdateView):
    model = MuscleExercise
    template_name = 'update.html'
    form_class = MuscleExerciseForm
    success_url = reverse_lazy('list')