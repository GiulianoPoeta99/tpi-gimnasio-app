from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine.model import Rutine


class RutineDeleteView(DeleteView):
    model = Rutine
    template_name = 'delete.html'
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirmar eliminación de rutina'
        return context
