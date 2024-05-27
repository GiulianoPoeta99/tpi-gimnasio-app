
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.progress.model import Progress


class ProgressDeleteView(UserPassesTestMixin, DeleteView):
    model = Progress
    template_name = 'progress_delete.html'
    success_url = reverse_lazy('progress_list')

    def test_func(self):
        return self.request.user.is_staff