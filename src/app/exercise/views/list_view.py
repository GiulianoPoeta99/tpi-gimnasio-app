from django.views.generic import ListView

from app.rutine.model import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'list.html'
    context_object_name = 'exercises'