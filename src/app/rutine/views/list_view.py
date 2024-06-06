from django.views.generic import ListView

from app.rutine.model import Rutine

class RutineListView(ListView):
    model = Rutine
    template_name = 'rutine/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return Rutine.objects.values('id', 'name', 'rutine_type__name', 'difficulty_level__name', 'user__first_name').order_by(*self.ordering)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Listado de rutinas.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas'}
        ]
        context['field_labels'] = {
            'id': 'N° de referencia',
            'name': Rutine._meta.get_field('name').verbose_name,
            'rutine_type__name': Rutine._meta.get_field('rutine_type').verbose_name,
            'difficulty_level__name': Rutine._meta.get_field('difficulty_level').verbose_name,
            'user__first_name': Rutine._meta.get_field('user').verbose_name,
        }
        queryset = self.get_queryset()
        if queryset.exists():
            context['headers'] = [context['field_labels'][field] for field in queryset[0].keys()]
        else:
            context['headers'] = []
        context['rows'] = list(self.get_queryset().values_list('id', 'name', 'rutine_type__name', 'difficulty_level__name', 'user__first_name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'info',
                    'url': 'rutine_detail',
                    'icon': 'eye',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'rutine_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'danger',
                    'url': 'rutine_delete',
                    'icon': 'trash',
                    'pk': True
                },
            ],
        }

        return context