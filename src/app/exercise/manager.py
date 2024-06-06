import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError,ObjectDoesNotExist

logger = logging.getLogger(__name__)

class ExerciseManager(models.Manager):
    def get_all(self):
        return self.all()
    
    def get_by_id(self, exercise_id):
        try:
            return self.get(id=exercise_id)
        except self.model.DoesNotExist:
            logger.error(f"Ejercicio con ID {exercise_id} no existe.")
            raise ObjectDoesNotExist("El ejercicio con el ID especificado no existe.")
    
    def create(self, name, user, difficulty_level = None, exercise_type = None):
        try:
            with transaction.atomic():
                exercise = self.model(name=name, user=user, difficulty_level=difficulty_level)
                exercise.full_clean()
                exercise.save()
                if exercise_type:
                    exercise.exercise_type.set(exercise_type)
                return exercise
        except ValidationError as e:
            logger.error(f"Error de validación al crear el ejercicio: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear ejercicio: {str(e)}")
            raise Exception(str(e))
        
    def update(self, exercise_id, name = None, user = None, difficulty_level = None, exercise_type = None):
        exercise =  self.get_by_id(exercise_id)

        try:
            with transaction.atomic():
                if name:
                    exercise.name = name
                if user:
                    exercise.user = user
                if difficulty_level:
                    exercise.difficulty_level = difficulty_level
                if exercise_type is not None:
                    exercise.exercise_type.set(exercise_type)

                exercise.full_clean()
                exercise.save()
                return exercise
        except ValidationError as e:
            logger.error(f"Error de validación al actualizar el ejercicio: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar ejercicio: {str(e)}")
            raise Exception(str(e))
        
    def delete(self, exercise_id):
        exercise = self.get_by_id(exercise_id)

        try:
            with transaction.atomic():
                exercise.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar el ejercicio con ID {exercise_id}: {str(e)}")
            raise Exception(str(e))