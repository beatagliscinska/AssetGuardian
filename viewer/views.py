from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from logging import getLogger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from viewer.models import Asset, Employee
from viewer.form import AssetForm

LOGGER = getLogger()


class AssetView(ListView):
    template_name = 'assets.html'
    model = Asset

class EmployeeView(ListView):
    template_name = 'employees.html'
    model = Employee


class AssetCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = AssetForm
    success_url = reverse_lazy('assets')
    permission_required = 'viewer.add_asset'

    def get_context_data(self, **kwargs):  # method to provide additional data to the template
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Add asset'
        return context

    def form_invalid(self, form):
        LOGGER.warning(">>>>>>User provided incorrect data.")
        return super().form_invalid(form)


class AssetUpdateView(PermissionRequiredMixin, UpdateView):
    model = Asset
    template_name = 'form.html'
    form_class = AssetForm
    success_url = reverse_lazy('assets')
    permission_required = 'viewer.update_asset'

    def get_context_data(self, **kwargs):  # method to provide additional data to the template
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Update'
        return context


class AssetDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'asset_confirm_delete.html'
    model = Asset
    success_url = reverse_lazy('assets')
    permission_required = 'viewer.delete_asset'





