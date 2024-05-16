from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from ..models import User  # Importa el modelo de usuario personalizado

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'user/user_form.html'
    
    def get_success_url(self):
        return reverse_lazy('construction')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'Username already exists.')
            return self.form_invalid(form)
        if User.objects.filter(email=email).exists():
            messages.error(self.request, 'Email already exists.')
            return self.form_invalid(form)
        # Encriptar la contraseña
        form.instance.set_password(form.cleaned_data.get('password'))
        return super().form_valid(form)
