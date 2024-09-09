import django_filters
from django_filters import rest_framework as filters

from catalog.models import Products


class ProductsFilter(django_filters.FilterSet):
    value = filters.CharFilter(
        field_name='parameter__value', lookup_expr='icontains'
    )

    class Meta:
        model = Products
        fields = [
            'name',
            'value',
        ]
