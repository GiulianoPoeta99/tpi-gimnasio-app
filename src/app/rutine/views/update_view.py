from django.views.generic import UpdateView
from django.urls import reverse_lazy
from app.rutine.form import RutineForm
from app.rutine.model import Rutine


class RutineUpdateView(UpdateView):
    model = Rutine
    template_name = 'update.html'
    form_class = RutineForm
    success_url = reverse_lazy('index')
