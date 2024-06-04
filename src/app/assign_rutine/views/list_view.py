from django.views.generic import ListView

from app.assign_rutine.model import AssignRutine

class RutineListView(ListView):
    model = AssignRutine
    template_name = 'assign_rutine/list.html'
    context_object_name = 'assign rutines'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de asignaciones de rutinas'
        return context
