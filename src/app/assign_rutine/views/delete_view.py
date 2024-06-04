from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.assign_rutine.model import AssignRutine


class RutineTypeDeleteView(DeleteView):
    model = AssignRutine
    template_name = 'assign_rutine/delete.html'
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirmar eliminación de asignación de rutina'
        return context
