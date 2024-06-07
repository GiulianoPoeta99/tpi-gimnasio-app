from django.views.generic import ListView
from app.rutine.model import Rutine

class RutineListView(ListView):
    model = Rutine
    template_name = 'rutine/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return Rutine.objects.get_default_table()

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Listado de todas las rutinas.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° de Referencia', "Nombre", 'Nivel de Dificultad', "Tipos", 'Creador',]
        context['rows'] = queryset.values_list(
            'id',
            'name',
            'difficulty_level_name',
            'rutine_types',
            'full_name'
        )
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'rutine_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'rutine_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'rutine_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context
