from django.db import models

from app.exercise_type.models import ExerciseType
from app.difficulty_level.models import DifficultyLevel
from app.user.model import User

# Create your models here.
class Exercise (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    type_id = models.ForeignKey(ExerciseType, on_delete=models.RESTRICT)
    dificulty_level_id = models.ForeignKey(DifficultyLevel, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='exercises')