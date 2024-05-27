from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.trainer.model import Trainer
from app.trainer.form import TrainerForm

class TrainerUpdateView(UserPassesTestMixin, UpdateView):
    model = Trainer
    template_name = 'trainer_form.html'
    form_class = TrainerForm
    success_url = reverse_lazy('trainer_list')

    def test_func(self):
        return self.request.user.is_staff # Solo permite acceso a la vista de entrenador si es admin , esto lo tenemos que cambiar a algun atributo que diga si es entrenador o no , pero hay que ver si lo ponemos en el registro o que 