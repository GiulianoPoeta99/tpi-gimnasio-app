from django.views.generic import DetailView

from app.exercise.model import Exercise

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'detail.html'
    context_object_name = 'exercise'