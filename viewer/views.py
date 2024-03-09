from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .filters import AssetFilter
from logging import getLogger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from viewer.models import Asset, Employee
from viewer.form import AssetForm, EmployeeForm
from django.core.exceptions import PermissionDenied

LOGGER = getLogger()


def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)


class AssetView(ListView):
    template_name = 'assets.html'
    model = Asset
    filterset_class = AssetFilter
    # permission_required = 'viewer.add_asset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_instance = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter_instance
        return context


class EmployeeView(PermissionRequiredMixin, ListView):
    template_name = 'employees.html'
    model = Employee
    permission_required = 'viewer.add_asset'


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Update'
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied("You do not have permission to delete and update assets.")
        return super().dispatch(request, *args, **kwargs)


class AssetDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'asset_confirm_delete.html'
    model = Asset
    success_url = reverse_lazy('assets')
    permission_required = 'viewer.delete_asset'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied("You do not have permission to delete and update assets.")
        return super().dispatch(request, *args, **kwargs)


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_em.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')
    permission_required = 'viewer.add_employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Add Employee'
        return context

    def form_invalid(self, form):
        LOGGER.warning(">>>>>>User provided incorrect data.")
        return super().form_invalid(form)


class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = Employee
    template_name = 'form_em.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')
    permission_required = 'viewer.update_employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Update'
        return context


class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'employee_confirm_delete.html'
    model = Employee
    success_url = reverse_lazy('employees')
    permission_required = 'viewer.delete_employee'
