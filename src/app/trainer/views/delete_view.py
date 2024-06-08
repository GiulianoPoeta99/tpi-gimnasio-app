from django.urls import reverse_lazy
from django.views.generic import DeleteView
from app.trainer.model import Trainer

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer/delete.html'
    success_url = reverse_lazy('trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Entrenadores'
        context['description'] = 'Eliminar un entrenador específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Entrenadores', 'url': 'trainer_list'},
            {'name': 'Eliminar'}
        ]
        return context
