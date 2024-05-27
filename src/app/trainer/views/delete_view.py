from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.trainer.model import Trainer

class TrainerDeleteView(UserPassesTestMixin, DeleteView):
    model = Trainer
    template_name = 'trainer_delete.html'
    success_url = reverse_lazy('trainer_list')

    def test_func(self):
        return self.request.user.is_staff