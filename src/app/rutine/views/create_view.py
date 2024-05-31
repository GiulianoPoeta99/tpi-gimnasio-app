from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.rutine.form import RutineForm
from app.rutine.model import Rutine

class RutineCreateView(CreateView):
    model = Rutine
    template_name = 'rutine/create.html'
    form_class = RutineForm

    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva rutina'
        return context