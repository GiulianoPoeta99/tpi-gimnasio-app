from django.urls import path

import app.rutine.views as view

urlpatterns = [
    path('', view.RutineListView.as_view(), name='list'),
    path('<int:pk>/', view.RutineDetailView.as_view(), name='detail'),
    path('create/', view.RutineCreateView.as_view(), name='create'),
    path('update/<int:pk>', view.RutineUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', view.RutineDeleteView.as_view(), name='delete'),
]
