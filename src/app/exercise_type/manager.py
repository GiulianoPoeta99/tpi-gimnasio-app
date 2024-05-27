import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class ExerciseTypeManager(models.Manager):
    def get_all(self):
        return self.all()
    
    def get_by_id(self, exercise_type_id):
        try:
            return self.get(id=exercise_type_id)
        except self.model.DoesNotExist:
            logger.error(f"Tipo de ejercicio con ID {exercise_type_id} no existe.")
            raise ObjectDoesNotExist("El tipo de ejercicio con el ID especificado no existe.")
        
    def create(self, name):
        try: 
            with transaction.atomic():
                exercise_type = self.model(name=name)
                exercise_type.full_clean()
                exercise_type.save()
                return exercise_type
        except ValidationError as e:
            logger.error(f"Error de validacion al crear el tipo de ejercicio: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear el tipo de ejercicio: {str(e)}")
            raise Exception(str(e))
    
    def update(self, exercise_type_id, name=None):
        exercise_type = self.get_by_id(exercise_type_id)

        try:
            with transaction.atomic():
                if name:
                    exercise_type.name = name

                exercise_type.full_clean()
                exercise_type.save()
                return exercise_type
        except ValidationError as e:
            logger.error(f"Error de validacion al actualizar el tipo de ejercicio: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar el tipo de ejercicio: {str(e)}")
            raise Exception(str(e))
    
    def delete(self, exercise_type_id):
        exercise_type = self.get_by_id(exercise_type_id)

        try:
            with transaction.atomic():
                exercise_type.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar el tipo de ejercicio con ID{exercise_type_id}: {str(e)}")
            raise Exception(str(e))