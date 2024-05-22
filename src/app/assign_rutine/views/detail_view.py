from django.views.generic import DetailView

from app.assign_rutine.model import AssignRutine

class RutineDetailView(DetailView):
    model = AssignRutine
    template_name = 'detail.html'
    context_object_name = 'rutine'
