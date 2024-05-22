import logging
from django.db import models, transaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist

logger = logging.getLogger(__name__)

class AssignRutineManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_id(self, assign_rutine_id):
        try:
            return self.get(id=assign_rutine_id)
        except self.model.DoesNotExist:
            logger.error(f"Asignación de rutina con ID {assign_rutine_id} no existe.")
            raise ObjectDoesNotExist("La asignación de rutina con el ID especificado no existe.")

    def create(self, user, trainer, rutine):
        try:
            with transaction.atomic():
                assign_rutine = self.model(user=user, trainer=trainer, rutine=rutine)
                assign_rutine.full_clean()
                assign_rutine.save()
                return assign_rutine
        except ValidationError as e:
            logger.error(f"Error de validación al crear asignación de rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al crear asignación de rutina: {str(e)}")
            raise Exception(str(e))

    def update(self, assign_rutine_id, user=None, trainer=None, rutine=None):
        assign_rutine = self.get_by_id(assign_rutine_id)

        try:
            with transaction.atomic():
                if user:
                    assign_rutine.user = user
                if trainer:
                    assign_rutine.trainer = trainer
                if rutine:
                    assign_rutine.rutine = rutine

                assign_rutine.full_clean()
                assign_rutine.save()
                return assign_rutine
        except ValidationError as e:
            logger.error(f"Error de validación al actualizar asignación de rutina: {e.message_dict}")
            raise ValidationError(e.message_dict)
        except Exception as e:
            logger.error(f"Error inesperado al actualizar asignación de rutina: {str(e)}")
            raise Exception(str(e))

    def delete(self, assign_rutine_id):
        assign_rutine = self.get_by_id(assign_rutine_id)

        try:
            with transaction.atomic():
                assign_rutine.delete()
                return True
        except Exception as e:
            logger.error(f"Error al eliminar asignación de rutina con ID {assign_rutine_id}: {str(e)}")
            raise Exception(str(e))
