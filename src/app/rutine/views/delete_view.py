from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine.model import Rutine

class RutineDeleteView(LoginRequiredMixin, DeleteView):
    model = Rutine
    template_name = 'rutine/delete.html'
    success_url = reverse_lazy('rutine_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Eliminar una rutina específica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas', 'url': 'rutine_list'},
            {'name': 'Eliminar'}
        ]
        return context
