from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.rutine_type.form import RutineTypeForm
from app.rutine_type.model import RutineType


class RutineTypeCreateView(CreateView):
    model = RutineType
    template_name = 'create.html'
    form_class = RutineTypeForm
    success_url = reverse_lazy('index')
