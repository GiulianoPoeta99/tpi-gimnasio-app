from django.urls import path
import app.user.views as view
from app.user.views.sign_up_view import SignUpView
from app.user.views.login_view import UserLoginView
from app.user.views.construction_view import ConstructionView

urlpatterns = [
    path('', view.UserListView.as_view(), name='user_list'),
    path('create/', SignUpView.as_view(), name='user_create'),
    path('<int:pk>/edit/', view.UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', view.UserDeleteView.as_view(), name='user_delete'),
    path('<int:pk>/', view.UserDetailView.as_view(), name='user_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
