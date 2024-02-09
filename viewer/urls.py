from django.urls import path
from viewer.views import AssetView, TemplateView

urlpatterns = [
       path('assets/', AssetView.as_view(), name='assets'),
       path('', TemplateView.as_view(template_name='home.html'), name='home')
]

