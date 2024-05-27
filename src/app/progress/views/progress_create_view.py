from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.progress.model import Progress
from app.progress.form import ProgressForm


class ProgressCreateView(UserPassesTestMixin, CreateView):
    model = Progress
    template_name = 'progress_form.html'
    form_class = ProgressForm
    success_url = reverse_lazy('progress_list')

    def test_func(self):
        return self.request.user.is_staff   