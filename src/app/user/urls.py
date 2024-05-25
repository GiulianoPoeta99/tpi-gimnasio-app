from django.urls import path
import app.user.views as view
from app.user.views.sign_up_view import SignUpView
from app.user.views.login_view import UserLoginView
from app.user.views.construction_view import ConstructionView
from app.user.views.home_view import HomeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', SignUpView.as_view(), name='user_create'),
    path('<int:pk>/edit/', view.UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', view.UserDeleteView.as_view(), name='user_delete'),
    path('<int:pk>/', view.UserDetailView.as_view(), name='user_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='user_logout'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
