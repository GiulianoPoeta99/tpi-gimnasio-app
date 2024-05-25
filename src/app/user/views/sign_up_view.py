from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from app.user.model import User
from app.user.form import SignUpForm

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Autenticar y hacer login al usuario
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Error de autenticación.')
        
        return response
