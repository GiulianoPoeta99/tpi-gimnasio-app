from django.urls import path
from app.home.views.dashboard_view import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
