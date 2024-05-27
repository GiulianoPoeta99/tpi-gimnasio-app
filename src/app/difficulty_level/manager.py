import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class DifficultyLevelManager(models.Manager):
    def get_all(self):
        return self.all()
    
    def get_by_id(self, difficulty_level_id):
        try:
            return self.get(id=difficulty_level_id)
        except self.model.DoesNotExist:
            logger.error(f"Nivel de dificultad con ID {difficulty_level_id} no existe.")
            raise ObjectDoesNotExist("Nivel de dificultad con el ID especificado no existe.")
    
    def create(self, name):
        try:
            with transaction.atomic():
                difficulty_level = self.model(name=name)
                difficulty_level.full_clean()
                difficulty_level.save()
                return difficulty_level
        except ValidationError as e:
            logger.error(f"Error de validación al crear el nivel de dificultad: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear el nivel de dificultad: {str(e)}")
            raise Exception(str(e))
    
    def update(self, difficulty_level_id, name=None):
        difficulty_level = self.get_by_id(difficulty_level_id)

        try:
            with transaction.atomic():
                if name:
                    difficulty_level.name = name

                difficulty_level.full_clean()
                difficulty_level.save()
                return difficulty_level
        except ValidationError as e:
            logger.error(f"Error de validación al actualizar nivel de dificultada: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar nivel de dificultad: {str(e)}")
            raise Exception(str(e))
        
    def delete(self, difficulty_level_id):
        difficulty_level = self.get_by_id(difficulty_level_id)

        try:
            with transaction.atomic():
                difficulty_level.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar el nivel de dificultad con ID {difficulty_level_id}: {str(e)}") 
            raise Exception(str(e))
        