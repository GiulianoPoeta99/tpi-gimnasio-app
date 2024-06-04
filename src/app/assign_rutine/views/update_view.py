from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.assign_rutine.form import AssignRutineForm
from app.assign_rutine.model import AssignRutine

class RutineUpdateView(UpdateView):
    model = AssignRutine
    template_name = 'assign_rutine/update.html'
    form_class = AssignRutineForm

    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar asignación de rutina'
        return context
