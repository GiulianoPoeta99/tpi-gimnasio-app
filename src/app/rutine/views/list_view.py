from django.views.generic import ListView

from app.rutine.model import Rutine

class RutineListView(ListView):
    model = Rutine
    template_name = 'list.html'
    context_object_name = 'rutines'
