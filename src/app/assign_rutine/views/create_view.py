from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.assign_rutine.form import AssignRutineForm
from app.assign_rutine.model import AssignRutine


class RutineCreateView(CreateView):
    model = AssignRutine
    template_name = 'assign_rutine/create.html'
    form_class = AssignRutineForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva asignación de rutina'
        return context
