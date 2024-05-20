from django.views.generic.detail import DetailView

from app.user.model import User

class UserDetailView(DetailView):
    model = User
    template_name = 'detail.html'
    context_object_name = 'user'
