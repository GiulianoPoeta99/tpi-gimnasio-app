from django.urls import path
from app.trainer.views.create_view import TrainerCreateView
from app.trainer.views.list_view import TrainerListView
from app.trainer.views.detail_view import TrainerDetailView
from app.trainer.views.update_view import TrainerUpdateView
from app.trainer.views.delete_view import TrainerDeleteView
urlpatterns = [
    path('', TrainerListView.as_view(), name='trainer_list'),
    path('<int:pk>/', TrainerDetailView.as_view(), name='trainer_detail'),
    path('create/', TrainerCreateView.as_view(), name='trainer_create'),
    path('update/<int:pk>/', TrainerUpdateView.as_view(), name='trainer_update'),
    path('delete/<int:pk>/', TrainerDeleteView.as_view(), name='trainer_delete'),
]
