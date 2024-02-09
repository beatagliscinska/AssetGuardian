from django.urls import path
from viewer.views import AssetView

urlpatterns = [
       path('assets/', AssetView.as_view(), name='assets')
]

