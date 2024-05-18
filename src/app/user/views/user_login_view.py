from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('construction')

    def form_invalid(self, form):
        # No agregar el mensaje aquí para evitar duplicación
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(request, 'Invalid email or password.', extra_tags='error')
            return self.form_invalid(self.get_form())

    def get_form(self):
        return super().get_form()
