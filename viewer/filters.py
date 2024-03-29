import django_filters
from viewer.models import Asset


class AssetFilter(django_filters.FilterSet):

    class Meta:
        model = Asset
        fields = ['category', 'description', 'vendor', 'serial_number', 'value', 'assigned_to', 'purchase_date']