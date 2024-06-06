from django.urls import path

import app.rutine.views as view

urlpatterns = [
    path('', view.RutineListView.as_view(), name='rutine_list'),
    path('<int:pk>/', view.RutineDetailView.as_view(), name='rutine_detail'),
    path('create/', view.RutineCreateView.as_view(), name='rutine_create'),
    path('update/<int:pk>/', view.RutineUpdateView.as_view(), name='rutine_update'),
    path('delete/<int:pk>/', view.RutineDeleteView.as_view(), name='rutine_delete'),
]
