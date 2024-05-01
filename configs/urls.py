from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.cars.urls')),
]
