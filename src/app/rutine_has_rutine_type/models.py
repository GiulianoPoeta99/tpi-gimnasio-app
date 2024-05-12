from django.db import models
from app.rutine.models import Rutine
from app.rutine_type.models import RutineType

class RutineHasRutineType(models.Model):
    rutine_id = models.ForeignKey(Rutine , on_delete=models.RESTRICT)
    rutine_type_id = models.ForeignKey(RutineType , on_delete=models.RESTRICT)