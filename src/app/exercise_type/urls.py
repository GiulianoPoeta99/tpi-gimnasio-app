from django.urls import path

import app.exercise_type.views as view

urlpatterns = [
    path('', view.ExerciseTypeListView.as_view(), name='index'),
    path('<int:pk>/', view.ExerciseTypeDetailView.as_view(), name='detail'),
    path('create/', view.ExerciseTypeCreateView.as_view(), name='create'),
    path('update/<int:pk>', view.ExerciseTypeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', view.ExerciseTypeDeleteView.as_view(), name='delete'),
]