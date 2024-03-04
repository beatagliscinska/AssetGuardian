from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django_filters.views import FilterView
from .filters import AssetFilter
from logging import getLogger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from viewer.models import Asset, Employee
from viewer.form import AssetForm, EmployeeForm

LOGGER = getLogger()


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

    def get_queryset(self):
        queryset = super().get_queryset()

        # Sorting
        sort_by = self.request.GET.get('sort_by', 'id')
        sort_order = self.request.GET.get('sort_order', 'asc')

        if sort_order == 'desc':
            sort_by = f'-{sort_by}'

        queryset = queryset.order_by(sort_by)

        return queryset


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

    def get_context_data(self, **kwargs):  # method to provide additional data to the template
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Update'
        return context


class AssetDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'asset_confirm_delete.html'
    model = Asset
    success_url = reverse_lazy('assets')
    permission_required = 'viewer.delete_asset'


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_em.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')
    permission_required = 'viewer.add_employee'

    def get_context_data(self, **kwargs):  # method to provide additional data to the template
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

    def get_context_data(self, **kwargs):  # method to provide additional data to the template
        context = super().get_context_data(**kwargs)
        context['submit_label'] = 'Update'
        return context


class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'employee_confirm_delete.html'
    model = Employee
    success_url = reverse_lazy('employees')
    permission_required = 'viewer.delete_employee'

