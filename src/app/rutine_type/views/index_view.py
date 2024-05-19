from django.views.generic import ListView

from app.rutine_type.model import RutineType

class RutineTypeIndexView(ListView):
    model = RutineType
    template_name = 'index.html'
    context_object_name = 'rutines'
