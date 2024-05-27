from django.views.generic import DetailView

from app.rutine_type.model import RutineType


class RutineTypeDetailView(DetailView):
    model = RutineType
    template_name = 'detail.html'
    context_object_name = 'rutine_type'
