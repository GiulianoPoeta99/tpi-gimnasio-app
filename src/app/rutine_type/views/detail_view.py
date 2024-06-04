from django.views.generic import DetailView

from app.rutine_type.model import RutineType


class RutineTypeDetailView(DetailView):
    model = RutineType
    template_name = 'rutine_type/detail.html'
    context_object_name = 'rutine_type'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle tipo de rutina'
        return context
