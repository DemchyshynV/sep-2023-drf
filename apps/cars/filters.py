from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    print(query)
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)

            case 'year_gte':
                qs = qs.filter(year__gt=v)
            case 'year_gt':
                qs = qs.filter(year__gte=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'engine_gt':
                qs = qs.filter(engine__gt=v)
            case 'engine_gte':
                qs = qs.filter(engine__gte=v)
            case 'engine_lt':
                qs = qs.filter(engine__lt=v)
            case 'engine_lte':
                qs = qs.filter(engine__lte=v)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)

            case 'body_type_start':
                qs = qs.filter(body_type__istartswith=v)
            case 'body_type_end':
                qs = qs.filter(body_type__iendswith=v)
            case 'body_type_contains':
                qs = qs.filter(body_type__icontains=v)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if v not in fields:
                    raise ValidationError({'details': f'Please choice order from {", ".join(fields)}'})

                qs = qs.order_by(v)
            case _:
                raise ValidationError({'details': f'{k} is not allowed here'})
    return qs
