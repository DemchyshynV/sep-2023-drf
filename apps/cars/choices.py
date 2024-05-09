from django.db.models import TextChoices


class CarChoices(TextChoices):
    Hatchback = 'Hatchback'
    Sedan = 'Sedan'
    Coupe = 'Coupe'
    Jeep = 'Jeep'
    Wagon = 'Wagon'
