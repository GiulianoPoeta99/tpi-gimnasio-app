from django.urls import path

import app.assign_rutine.views as view

urlpatterns = [
    path('', view.AssignRutineListView.as_view(), name='index'),
    path('<int:pk>/', view.AssignRutineDetailView.as_view(), name='detail'),
    path('create/', view.AssignRutineCreateView.as_view(), name='create'),
    path('update/<int:pk>', view.AssignRutineUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', view.AssignRutineDeleteView.as_view(), name='delete'),
]
