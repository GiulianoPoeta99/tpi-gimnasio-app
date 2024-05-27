from django.urls import path
from app.progress.views.progress_create_view import ProgressCreateView
from app.progress.views.progress_delete_view import ProgressDeleteView
from app.progress.views.progress_detail_view import ProgressDetailView
from app.progress.views.progress_list_view   import ProgressListView
from app.progress.views.progress_update_view import ProgressUpdateView

urlpatterns = [
    path('', ProgressListView.as_view(), name='progress_list'),
    path('<int:pk>/', ProgressDetailView.as_view(), name='progress_detail'),
    path('create/', ProgressCreateView.as_view(), name='progress_create'),
    path('<int:pk>/update/', ProgressUpdateView.as_view(), name='progress_update'),
    path('<int:pk>/delete/', ProgressDeleteView.as_view(), name='progress_delete'),
]
