from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.difficulty_level.form import DifficultyLevelForm
from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelUpdateView(UpdateView):
    model = DifficultyLevel
    template_name = 'update.html'
    form_class = DifficultyLevelForm
    success_url = reverse_lazy('list')