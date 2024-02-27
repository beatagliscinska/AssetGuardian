from django.urls import path
from viewer.views import AssetView, AssetCreateView, AssetUpdateView, AssetDeleteView

urlpatterns = [
    path('', AssetView.as_view(template_name='home.html'), name='home'),
    path('asset/create', AssetCreateView.as_view(), name='asset_create'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
    path('asset/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete')
]
