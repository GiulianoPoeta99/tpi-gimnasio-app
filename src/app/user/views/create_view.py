from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from app.user.model import User

class UserUpdateView(CreateView):
    model = User
    fields = ['username', 'email', 'profile_profile']
    template_name = 'create.html'
    success_url = reverse_lazy('list')
