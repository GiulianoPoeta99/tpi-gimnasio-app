from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from app.rutine.model import Rutine

class RutineListView(LoginRequiredMixin, ListView):
    model = Rutine
    template_name = 'rutine/list.html'

    # override
    def get_queryset(self):
        return Rutine.objects.get_default_table().order_by(*self.model._meta.ordering)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural
        context['description'] = 'Listado de todas las rutinas.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas'}
        ]

        queryset = self.get_queryset()
        context['headers'] = [
            self.model._meta.get_field('name').verbose_name,
            self.model._meta.get_field('difficulty_level').verbose_name,
            self.model._meta.get_field('rutine_type').verbose_name,
            self.model._meta.get_field('user').verbose_name
        ]
        context['rows'] = queryset.values_list(
            'name',
            'difficulty_level_name',
            'rutine_types',
            'full_name'
        )
        return context
