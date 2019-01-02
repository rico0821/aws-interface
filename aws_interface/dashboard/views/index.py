from dashboard.views.view import DashboardView
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, View, DashboardView):
    def get(self, request):
        if self.is_login(request):
            redirect('apps')
        else:
            redirect('login')
