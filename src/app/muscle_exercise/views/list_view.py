from django.views.generic import ListView

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseListView(ListView):
    model = MuscleExercise
    template_name = 'index.html'
    context_object_name = 'muscle_exercises'