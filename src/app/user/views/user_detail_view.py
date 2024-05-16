from django.views.generic.detail import DetailView
from ..models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'
