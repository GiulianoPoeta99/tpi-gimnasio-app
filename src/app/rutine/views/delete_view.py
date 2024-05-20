from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine.model import Rutine


class RutineDeleteView(DeleteView):
    model = Rutine
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
