from django.views.generic import DetailView

from app.rutine_type.model import RutineType


class RutineTypeDetailView(DetailView):
    model = RutineType
    template_name = 'rutine_type/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Rutinas'
        context['description'] = 'Todos los detalles de un tipo de rutina especifica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas', 'url': 'rutine_type_list'},
            {'name': 'Detalle'}
        ]
        return context