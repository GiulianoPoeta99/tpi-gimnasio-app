from django.db import models

# Create your models here.
class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    