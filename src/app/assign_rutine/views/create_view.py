from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.assign_rutine.form import AssignRutineForm
from app.assign_rutine.model import AssignRutine


class RutineCreateView(CreateView):
    model = AssignRutine
    template_name = 'create.html'
    form_class = AssignRutineForm
    success_url = reverse_lazy('list')
