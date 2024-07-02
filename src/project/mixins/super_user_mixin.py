from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

class SuperAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser