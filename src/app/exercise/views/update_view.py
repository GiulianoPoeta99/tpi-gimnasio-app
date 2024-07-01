from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.exercise.form import ExerciseForm 
from app.exercise.model import Exercise

class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    template_name = 'update.html'
    form_class = ExerciseForm
   
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Ejercicios'
        context['description'] = 'Actualizar un ejercicio existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Ejercicios', 'url': 'exercise_list'},
            {'name': 'Actualizar'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('exercise_detail', kwargs={'pk': self.object.pk})