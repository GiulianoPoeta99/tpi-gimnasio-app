# app/user/views/user_login_view.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return reverse_lazy('construction')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)
