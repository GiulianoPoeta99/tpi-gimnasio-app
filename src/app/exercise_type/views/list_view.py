from django.views.generic import ListView

from app.exercise_type.model import ExerciseType

class ExerciseTypeListView(ListView):
    model = ExerciseType
    template_name = 'index.html'
    context_object_name = 'exercise_types'