from django.views.generic import DetailView

from app.exercise_type.model import ExerciseType

class ExerciseTypeDetailView(DetailView):
    model = ExerciseType
    template_name = 'detail.html'
    context_object_name = 'exercise_type'