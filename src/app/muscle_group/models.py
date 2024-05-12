from django.db import models
from app.exercise.models import Exercise
from app.muscle_exercise.models import MuscleExercise

# Create your models here.
class MuscleGroup(models.Model):
    exercise_id = models. ForeignKey(Exercise, on_delete=models.RESTRICT)
    muscle_exercise_id = models.ForeignKey(MuscleExercise, on_delete=models.RESTRICT)