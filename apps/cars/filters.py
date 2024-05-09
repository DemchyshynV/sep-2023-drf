from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year','lt')
    year_gt = filters.NumberFilter('year','gt')
    brand=filters.CharFilter('brand','icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'price',
            ('year', 'asd')
        )
    )