from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from app.user.model import User

class AdminDashboardView(UserPassesTestMixin, TemplateView):
    template_name = 'admin_dashboard.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
