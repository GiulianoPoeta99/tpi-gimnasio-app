from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.rutine.model import Rutine

class RutineDetailView(LoginRequiredMixin, DetailView):
    model = Rutine
    template_name = 'rutine/detail.html'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Todos los detalles de una rutina especifica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas', 'url': 'rutine_list'},
            {'name': 'Detalle'}
        ]
        return context