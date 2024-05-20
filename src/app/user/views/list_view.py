from django.views.generic.list import ListView

from app.user.model import User

class UserListView(ListView):
    model = User
    template_name = 'list.html'
    context_object_name = 'users'
