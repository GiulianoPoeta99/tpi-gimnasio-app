from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from ..models import User

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'profile_profile']
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user_list')
