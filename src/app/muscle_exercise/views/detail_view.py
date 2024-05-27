from django.views.generic import DetailView

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseDetailView(DetailView):
    model = MuscleExercise
    template_name = 'detail.html'
    context_object_name = 'muscle_exercise'