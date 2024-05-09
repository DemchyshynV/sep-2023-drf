from django.urls import path

from apps.auto_parks.views import AutoParkAddCarView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
]
