from django.urls import reverse_lazy
from django.views.generic import DeleteView
from app.progress.model import Progress

class ProgressDeleteView(DeleteView):
    model = Progress
    template_name = 'progress/delete.html'
    success_url = reverse_lazy('progress_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Progresos'
        context['description'] = 'Eliminar un progreso específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Progresos', 'url': 'progress_list'},
            {'name': 'Eliminar'}
        ]
        return context
