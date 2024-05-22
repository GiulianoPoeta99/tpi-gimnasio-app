from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.assign_rutine.model import AssignRutine


class RutineTypeDeleteView(DeleteView):
    model = AssignRutine
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
