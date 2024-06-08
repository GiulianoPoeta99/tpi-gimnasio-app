from django.urls import reverse_lazy
from django.views.generic import UpdateView
from app.trainer.form import TrainerForm
from app.trainer.model import Trainer

class TrainerUpdateView(UpdateView):
    model = Trainer
    template_name = 'trainer/update.html'
    form_class = TrainerForm

    def get_success_url(self):
        return reverse_lazy('trainer_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['title'] = 'Entrenadores'
        context['description'] = 'Actualizar un entrenador existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Entrenadores', 'url': 'trainer_list'},
            {'name': 'Actualizar'}
        ]
        return context
