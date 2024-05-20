from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from app.user.model import User

class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
