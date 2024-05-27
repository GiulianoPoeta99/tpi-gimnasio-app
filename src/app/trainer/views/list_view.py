from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.trainer.model import Trainer

class TrainerListView(UserPassesTestMixin, ListView):
    model = Trainer
    template_name = 'trainer_list.html'
    context_object_name = 'trainers'

    def test_func(self):
        return self.request.user.is_staff