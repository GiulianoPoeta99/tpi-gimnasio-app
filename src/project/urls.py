from django.contrib import admin
from django.urls import path, include

from app.user.views.home_view import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('user/', include('app.user.urls')),
    path('rutine/', include('app.rutine.urls')),
    path('rutine-type/', include('app.rutine_type.urls')),
]
