from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.rutine.form import RutineForm
from app.rutine.model import Rutine

class RutineUpdateView(UpdateView):
    model = Rutine
    template_name = 'update.html'
    form_class = RutineForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar rutina'
        return context