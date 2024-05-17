from django.views.generic import DetailView
from app.rutine.model import Rutine


class RutineDetailView(DetailView):
    model = Rutine
    template_name = 'detail.html'
    context_object_name = 'rutine'
