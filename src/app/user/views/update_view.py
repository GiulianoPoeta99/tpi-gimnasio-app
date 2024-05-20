from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from app.user.model import User

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'profile_profile']
    template_name = 'update.html'
    success_url = reverse_lazy('list')
