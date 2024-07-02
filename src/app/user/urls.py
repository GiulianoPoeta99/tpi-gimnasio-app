from django.urls import path
import app.user.views as view
from app.user.views.list_view import UserListView
from app.user.views.update_view import UserUpdateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', view.UserDetailView.as_view(), name='user_detail'),
    # path('create/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>', view.UserDeleteView.as_view(), name='user_delete'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
]
