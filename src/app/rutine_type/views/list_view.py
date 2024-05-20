from django.views.generic import ListView

from app.rutine_type.model import RutineType

class RutineTypeListView(ListView):
    model = RutineType
    template_name = 'index.html'
    context_object_name = 'rutines'
