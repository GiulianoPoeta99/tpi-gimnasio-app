from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.progress.model import Progress


class ProgressListView(UserPassesTestMixin, ListView):
    model = Progress
    template_name = 'progress_list.html'
    context_object_name = 'progresses'

    def test_func(self):
        return self.request.user.is_staff