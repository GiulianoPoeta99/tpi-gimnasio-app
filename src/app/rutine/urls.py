from django.urls import path

import app.rutine.views as view

urlpatterns = [
    path('', view.RutineListView.as_view(), name='rutine_list'),
    path('own/', view.OwnRutineListView.as_view(), name='own_rutine_list'),
    path('<int:pk>/', view.RutineDetailView.as_view(), name='rutine_detail'),
    path('detail/<int:pk>/', view.OwnRutineDetailView.as_view(), name='own_rutine_detail'),
    path('create/', view.RutineCreateView.as_view(), name='rutine_create'),
    path('update/<int:pk>/', view.RutineUpdateView.as_view(), name='rutine_update'),
    path('add-exercises/<int:pk>/', view.AddExercisesView.as_view(), name='rutine_add_exercises'),
]
