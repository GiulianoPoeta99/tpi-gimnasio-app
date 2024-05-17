import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class RutineManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_id(self, rutine_id):
        try:
            return self.get(id=rutine_id)
        except self.model.DoesNotExist:
            logger.error(f"Rutina con ID {rutine_id} no existe.")
            raise ObjectDoesNotExist("La rutina con el ID especificado no existe.")

    def create(self, name, user, difficulty_level = None, rutine_types = None):
        try:
            with transaction.atomic():
                rutine = self.model(name=name, user=user, difficulty_level=difficulty_level)
                rutine.full_clean()
                rutine.save()
                if rutine_types:
                    rutine.rutine_type.set(rutine_types)
                return rutine
        except ValidationError as e:
            logger.error(f"Error de validación al crear rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear rutina: {str(e)}")
            raise Exception(str(e))

    def update(self, rutine_id , name = None, user = None, difficulty_level = None, rutine_types = None):
        rutine = self.get_by_id(rutine_id)

        try:
            with transaction.atomic():
                if name:
                    rutine.name = name
                if user:
                    rutine.user = user
                if difficulty_level:
                    rutine.difficulty_level = difficulty_level
                if rutine_types is not None:
                    rutine.rutine_type.set(rutine_types)

                rutine.full_clean()
                rutine.save()
                return rutine
        except ValidationError as e:
            logger.error(f"Error de validación al actualizar rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar rutina: {str(e)}")
            raise Exception(str(e))

    def delete(self, rutine_id):
        rutine = self.get_by_id(rutine_id)

        try:
            with transaction.atomic():
                rutine.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar rutina con ID {rutine_id}: {str(e)}")
            raise Exception(str(e))