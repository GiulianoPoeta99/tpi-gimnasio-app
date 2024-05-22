from django.views.generic import ListView

from app.assign_rutine.model import AssignRutine

class RutineListView(ListView):
    model = AssignRutine
    template_name = 'list.html'
    context_object_name = 'rutines'
