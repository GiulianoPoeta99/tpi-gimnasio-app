# app/user/views/user_list_view.py
from django.views.generic.list import ListView
from ..models import User

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
