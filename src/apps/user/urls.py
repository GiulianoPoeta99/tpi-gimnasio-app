from django.urls import path
from .views import UserCreateView , UserUpdateView , UserDetailView , HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/',UserCreateView.as_view(), name='user_create'),
    path('edit/<int:pk>/',UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
