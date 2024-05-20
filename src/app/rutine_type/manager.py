import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class RutineTypeManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_id(self, rutine_type_id):
        try:
            return self.get(id=rutine_type_id)
        except self.model.DoesNotExist:
            logger.error(f"Tipo de rutina con ID {rutine_type_id} no existe.")
            raise ObjectDoesNotExist("El tipo de rutina con el ID especificado no existe.")

    def create(self, name):
        try:
            with transaction.atomic():
                rutine_type = self.model(name=name)
                rutine_type.full_clean()
                rutine_type.save()
                return rutine_type
        except ValidationError as e:
            logger.error(f"Error de validación al crear tipo de rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear tipo de rutina: {str(e)}")
            raise Exception(str(e))

    def update(self, rutine_type_id, name=None):
        rutine_type = self.get_by_id(rutine_type_id)

        try:
            with transaction.atomic():
                if name:
                    rutine_type.name = name

                rutine_type.full_clean()
                rutine_type.save()
                return rutine_type
        except ValidationError as e:
            logger.error(f"Error de validación al actualizar tipo de rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar tipo de rutina: {str(e)}")
            raise Exception(str(e))

    def delete(self, rutine_type_id):
        rutine_type = self.get_by_id(rutine_type_id)

        try:
            with transaction.atomic():
                rutine_type.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar tipo de rutina con ID {rutine_type_id}: {str(e)}")
            raise Exception(str(e))
