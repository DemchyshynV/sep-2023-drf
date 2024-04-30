from django.urls import path
from cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # # path('carDetail/<int:pk>', CarDetailView.as_view()),
    # path('carDetail/<slug:pk>', CarDetailView.as_view()),
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]
