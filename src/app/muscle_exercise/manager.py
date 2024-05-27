import logging
from django.db import models,transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class MuscleExerciseManager(models.Manager):
    def get_all(self):
        return self.all()
    
    def get_by_id(self, muscle_exercise_id):
        try:
            return self.get(id=muscle_exercise_id)
        except self.model.DoesNotExist:
            logger.error(f"Tipo de ejercicio de musculo con ID{muscle_exercise_id} no existe.")
            raise ObjectDoesNotExist("El tipo de ejercicio de musculo con el ID especificado no existe.")
    
    def create(self, name):
        try:
            with transaction.atomic():
                muscle_exercise = self.model(name=name)
                muscle_exercise.full_clean()
                muscle_exercise.save()
                return muscle_exercise
        except ValidationError as e:
            logger.error(f"Error de validacion al crear tipo de rutina:{e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear tipo de ejercicio de musculo:{str(e)}")
            raise Exception(str(e))
    
    def update(self, muscle_exercise_id, name=None):
        muscle_exercise = self.get_by_id(muscle_exercise_id)

        try:
            with transaction.atomic():
                if name:
                    muscle_exercise.name = name

                muscle_exercise.full_clean()
                muscle_exercise.save()
        except ValidationError as e:
            logger.error(f"Error de validacion al actualizar el ejercicio de musculo: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar ejercicio de musculo: {str(e)}")
            raise Exception (str(e))
        
    def delete(self, muscle_exercise_id):
        muscle_exercise = self.get_by_id(muscle_exercise_id)

        try: 
            with transaction.atomic():
                muscle_exercise.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar el ejercicio de musculo con ID {muscle_exercise_id}: {str(e)}")
            raise Exception(str(e))