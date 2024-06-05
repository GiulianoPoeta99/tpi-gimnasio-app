from django.views.generic import ListView

from app.rutine.model import Rutine

class RutineListView(ListView):
    model = Rutine
    template_name = 'rutine/list.html'
    paginate_by = 20
    ordering = ['id']

    # override
    def get_queryset(self):
        return Rutine.objects.values('name', 'rutine_type__name', 'difficulty_level__name', 'user__first_name').order_by(*self.ordering)


    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas'
        context['description'] = 'Listado de rutinas'
        context['breadcrumb_items'] = [
            {'name': 'Dashboard', 'url': 'index.html'},
            {'name': 'Rutinas'}
        ]
        context['field_labels'] = {
            'name': Rutine._meta.get_field('name').verbose_name,
            'rutine_type__name': Rutine._meta.get_field('rutine_type').verbose_name,
            'difficulty_level__name': Rutine._meta.get_field('difficulty_level').verbose_name,
            'user__first_name': Rutine._meta.get_field('user').verbose_name,
        }

        # Obtener los headers de los campos si hay resultados
        queryset = self.get_queryset()
        if queryset.exists():
            context['headers'] = [context['field_labels'][field] for field in queryset[0].keys()]
        else:
            context['headers'] = []

        context['rows'] = list(self.get_queryset().values_list('name', 'rutine_type__name', 'difficulty_level__name', 'user__first_name'))

        return context