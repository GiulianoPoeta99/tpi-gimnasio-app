from django.db import models
from app.exercise.models import Exercise
from app.user.models import User


class ExerciseProgress(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.RESTRICT)
    id_exercise = models.ForeignKey(Exercise,on_delete=models.RESTRICT)
