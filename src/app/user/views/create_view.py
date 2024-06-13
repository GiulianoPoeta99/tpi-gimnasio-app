from django.urls import reverse_lazy
from django.views.generic import CreateView
from app.user.model import User
from app.user.form import UserForm

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        context['title'] = 'Usuarios'
        context['description'] = 'Crear un nuevo usuario.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Usuarios', 'url': 'user_list'},
            {'name': 'Crear'}
        ]
        return context