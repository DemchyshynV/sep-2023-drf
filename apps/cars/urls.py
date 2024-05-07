from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # # path('carDetail/<int:pk>', CarDetailView.as_view()),
    # path('carDetail/<slug:pk>', CarDetailView.as_view()),
    path('', CarListView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_delete'),
]
