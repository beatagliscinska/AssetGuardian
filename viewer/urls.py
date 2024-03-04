from django.urls import path
from viewer.views import AssetView, AssetCreateView, AssetUpdateView, AssetDeleteView
from viewer.views import EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView
from .views import permission_denied_view

urlpatterns = [
    path('', AssetView.as_view(template_name='home.html'), name='home'),
    path('asset/create', AssetCreateView.as_view(), name='asset_create'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
    path('asset/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),
    path('employee/create', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]


handler403 = permission_denied_view