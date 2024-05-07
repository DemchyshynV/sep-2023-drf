from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls')),
]
