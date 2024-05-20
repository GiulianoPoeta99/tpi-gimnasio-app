from django.urls import path

import app.rutine_type.views as view

urlpatterns = [
    path('', view.RutineTypeListView.as_view(), name='index'),
    path('<int:pk>/', view.RutineTypeDetailView.as_view(), name='detail'),
    path('create/', view.RutineTypeCreateView.as_view(), name='create'),
    path('update/<int:pk>', view.RutineTypeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', view.RutineTypeDeleteView.as_view(), name='delete'),
]
