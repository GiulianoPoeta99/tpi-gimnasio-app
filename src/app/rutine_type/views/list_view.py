from django.views.generic import ListView

from app.rutine_type.model import RutineType

class RutineTypeListView(ListView):
    model = RutineType
    template_name = 'rutine_type/list.html'
    context_object_name = 'rutine types'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos de rutinas'
        return context
