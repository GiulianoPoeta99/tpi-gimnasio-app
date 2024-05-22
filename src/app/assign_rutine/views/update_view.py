from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.assign_rutine.form import AssignRutineForm
from app.assign_rutine.model import AssignRutine

class RutineUpdateView(UpdateView):
    model = AssignRutine
    template_name = 'update.html'
    form_class = AssignRutine
    success_url = reverse_lazy('list')
