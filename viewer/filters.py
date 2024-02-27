import django_filters
from .models import Asset


class AssetFilter(django_filters.FilterSet):

    class Meta:
        model = Asset
        fields = ['asset_number', 'category', 'description', 'vendor', 'serial_number', 'value', 'assigned_to', 'purchase_date']