from django.views.generic import ListView

from app.rutine.model import Rutine

class RutineListView(ListView):
    model = Rutine
    template_name = 'rutine/list.html'
    context_object_name = 'rutines'
    paginate_by = 20
    ordering = ['id']

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Listado de rutinas'
        context['breadcrumb_items'] = [
            {'name': 'Dashboard', 'url': 'index.html'},
            {'name': 'Rutinas'}
        ]

        return context