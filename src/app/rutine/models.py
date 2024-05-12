from django.db import models
from app.user.models import User
from app.difficulty_level.models import DifficultyLevel
from app.rutine_type.models import RutineType

class Rutine(models.Model):
    name = models.CharField(max_length=60)
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    difficulty_level_id = models.ForeignKey(DifficultyLevel , on_delete=models.RESTRICT)
    rutine_type_id = models.ForeignKey(RutineType , on_delete=models.RESTRICT)