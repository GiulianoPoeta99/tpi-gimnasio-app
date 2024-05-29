from django.urls import path
from app.dashboard import views

urlpatterns = [
    path('', views.index, name='dashboard'),
]
