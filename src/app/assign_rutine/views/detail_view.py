from django.views.generic import DetailView

from app.assign_rutine.model import AssignRutine

class RutineDetailView(DetailView):
    model = AssignRutine
    template_name = 'assign_rutine/detail.html'
    context_object_name = 'assign rutine'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle asignar rutina'
        return context
