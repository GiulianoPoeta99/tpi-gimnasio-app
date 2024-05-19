from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine_type.model import RutineType


class RutineTypeDeleteView(DeleteView):
    model = RutineType
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
