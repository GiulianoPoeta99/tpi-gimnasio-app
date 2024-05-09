from django.db import models
from .exercise import Exercise
from .muscle_exercise import MuscleExercise

# Create your models here.
class MuscleGroup(models.Model):
    exercise = models. ForeignKey(Exercise, on_delete=models.RESTRICT, related_name='muscle_groups')
    muscle_exercise = models.ForeignKey(MuscleExercise, on_delete=models.RESTRICT)
    