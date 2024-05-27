from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.progress.model import Progress


class ProgressDetailView(UserPassesTestMixin, DetailView):
    model = Progress
    template_name = 'progress_detail.html'
    context_object_name = 'progress'

    def test_func(self):
        return self.request.user.is_staff