from django.views.generic import ListView

from app.rutine_type.model import RutineType

class RutineTypeListView(ListView):
    model = RutineType
    template_name = 'rutine_type/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return RutineType.objects.values('id', 'name').order_by(*self.ordering)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Rutinas'
        context['description'] = 'Listado de todos los tipos de rutinas.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas'}
        ]
        context['field_labels'] = {
            'id': 'N° de referencia',
            'name': RutineType._meta.get_field('name').verbose_name,
        }
        queryset = self.get_queryset()
        if queryset.exists():
            context['headers'] = [context['field_labels'][field] for field in queryset[0].keys()]
        else:
            context['headers'] = []
        context['rows'] = list(self.get_queryset().values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'rutine_type_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'rutine_type_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'rutine_type_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context