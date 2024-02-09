from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from logging import getLogger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from viewer.models import Asset


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'money', 'deadlines']}
    )


class AssetView(ListView):
    template_name = 'assets.html'
    model = Asset

