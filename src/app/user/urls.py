from django.urls import path
import app.user.views as view
from app.user.views.create_view import UserCreateView
from app.user.views.list_view import UserListView
from app.user.views.update_view import UserUpdateView
from app.home.views.sign_up_view import SignUpView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', view.UserDetailView.as_view(), name='user_detail'),
    path('create/', SignUpView.as_view(), name='user_create2'),
    path('createCrud/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', view.UserDeleteView.as_view(), name='user_delete'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
]
