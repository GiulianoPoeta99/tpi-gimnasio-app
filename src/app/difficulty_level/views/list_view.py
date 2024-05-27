from django.views.generic import ListView

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelListView(ListView):
    model = DifficultyLevel
    template_name = 'list.html'
    context_object_name = 'difficulty_levels'