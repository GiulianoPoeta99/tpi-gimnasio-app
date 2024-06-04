from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.rutine_type.form import RutineTypeForm
from app.rutine_type.model import RutineType


class RutineTypeCreateView(CreateView):
    model = RutineType
    template_name = 'create.html'
    form_class = RutineTypeForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nuevo tipo de rutina'
        return context
