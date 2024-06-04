from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine_type.model import RutineType


class RutineTypeDeleteView(DeleteView):
    model = RutineType
    template_name = 'rutine_type/delete.html'

    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirmar eliminación de tipo de rutina'
        return context
