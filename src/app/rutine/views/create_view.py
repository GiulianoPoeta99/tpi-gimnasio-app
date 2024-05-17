from django.views.generic import CreateView
from django.urls import reverse_lazy
from app.rutine.form import RutineForm
from app.rutine.model import Rutine


class RutineCreateView(CreateView):
    model = Rutine
    template_name = 'create.html'
    form_class = RutineForm
    success_url = reverse_lazy('index')
