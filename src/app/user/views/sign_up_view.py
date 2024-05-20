from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login

from app.user.model import User

class SignUpView(CreateView):
    model = User
    fields = ['first_name','last_name', 'email', 'password']
    template_name = 'sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('construction')
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(self.request, 'Email already exists.')
            return self.form_invalid(form)
        
        # Encriptar la contraseña
        form.instance.set_password(password)
        
        # Guardar el nuevo usuario
        response = super().form_valid(form)
        
        # Autenticar y hacer login al usuario
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Authentication failed.')
        
        return response
