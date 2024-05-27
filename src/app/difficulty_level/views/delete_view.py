from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelDeleteView(DeleteView):
    model = DifficultyLevel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')