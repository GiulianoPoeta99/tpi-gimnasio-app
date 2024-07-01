from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseListView(LoginRequiredMixin, ListView):
    model = MuscleExercise
    template_name = 'muscle_exercise/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return MuscleExercise.objects.get_default_table().order_by(*self.ordering)
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ['Musculos']
        context['description'] = 'Listado de todos los musculos.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name':'Musculos'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° de referencia', MuscleExercise._meta.get_field('name').verbose_name]
        context['rows'] = list(queryset.values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'muscle_exercise_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'muscle_exercise_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'muscle_exercise_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context