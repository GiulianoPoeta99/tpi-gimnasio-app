from django.urls import path , include
from app.dashboard import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('trainers/', include('app.trainer.urls')),
]
