from django.db import models
from .exercise_type import ExerciseType
from .dificulty_level import DifficultyLevel
from apps.user.models import User

# Create your models here.
class Exercise (models.Model):
    type = models.ForeignKey(ExerciseType, on_delete=models.RESTRICT, related_name='exercises')
    name = models.CharField(max_length=100)
    dificulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.RESTRICT)
    id_user = models.ForeignKey(User, on_delete=models.RESTRICT)
    