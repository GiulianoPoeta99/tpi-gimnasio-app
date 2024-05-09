from django.db import models

class DifficultyLevel(models.Model):
    name = models.CharField(max_length=100)

  