from django.views.generic import DetailView

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelDetailView(DetailView):
    model = DifficultyLevel
    template_name = 'detail.html'
    context_object_name = 'difficulty_level'