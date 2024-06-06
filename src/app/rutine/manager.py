import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class RutineManager(models.Manager):
    pass