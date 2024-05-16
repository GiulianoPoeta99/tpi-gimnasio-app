from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from ..models import User

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/confirm_delete.html'
    success_url = reverse_lazy('user_list')
