from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.rutine_type.form import RutineTypeForm
from app.rutine_type.model import RutineType


class RutineTypeUpdateView(UpdateView):
    model = RutineType
    template_name = 'rutine_type/update.html'
    form_class = RutineTypeForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar tipo de rutina'
        return context
