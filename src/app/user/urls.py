from django.urls import path
from .views.user_create_view import UserCreateView
from .views.user_update_view import UserUpdateView
from .views.user_delete_view import UserDeleteView
from .views.user_detail_view import UserDetailView
from .views.user_list_view import UserListView
from .views.user_login_view import UserLoginView
from .views.construction_view import ConstructionView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
