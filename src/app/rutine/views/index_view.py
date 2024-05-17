from django.views.generic import ListView
from app.rutine.model import Rutine

class RutineIndexView(ListView):
    model = Rutine
    template_name = 'index.html'
    context_object_name = 'rutines'
