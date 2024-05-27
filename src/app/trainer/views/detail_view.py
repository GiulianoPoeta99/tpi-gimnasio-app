from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.trainer.model import Trainer


class TrainerDetailView(UserPassesTestMixin, DetailView):
    model = Trainer
    template_name = 'trainer_detail.html'
    context_object_name = 'trainer'

    def test_func(self):
        return self.request.user.is_staff