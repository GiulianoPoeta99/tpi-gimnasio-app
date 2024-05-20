from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.rutine_type.form import RutineTypeForm
from app.rutine_type.model import RutineType


class RutineTypeUpdateView(UpdateView):
    model = RutineType
    template_name = 'update.html'
    form_class = RutineTypeForm
    success_url = reverse_lazy('list')
