from django.urls import path
from .views.home_view import HomeView
from app.home.views.dashboard_view import DashboardView
from .views.construction_view import ConstructionView
from .views.login_view import UserLoginView
from .views.sign_up_view import SignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('construction/', ConstructionView.as_view(), name='construction'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('signup/', SignUpView.as_view(), name='user_create'),
]
