from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.difficulty_level.form import DifficultyLevelForm
from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelView(CreateView):
    model = DifficultyLevel
    template_name = 'create.html'
    form_class = DifficultyLevelForm
    success_url = reverse_lazy('list')