from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import CarChoices


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)
    # brand = models.CharField(max_length=50, validators=[V.MinLengthValidator(3)])
    brand = models.CharField(max_length=50, validators=[V.RegexValidator('^[A-Z][a-zA-z]{2,49}$', [
        'first letter uppercase',
        'min 3',
        'max 50'
    ])])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    body_type = models.CharField(max_length=50, choices=[*CarChoices.choices])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')