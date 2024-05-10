from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView
from .models import User


class HomePageView(TemplateView):
    template_name = 'user/home.html'


class UserCreateView(CreateView):
    model = User
    fields = ['username','email','password','profile_picture']
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user_detail')


class UserUpdateView(UpdateView):
    model = User
    fields = ['email','profile_picture']
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user_detail')

class UserDetailView(DeleteView):
    model: User
    template_name = 'user/user_detail.html'