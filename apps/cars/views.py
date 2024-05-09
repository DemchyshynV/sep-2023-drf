from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from apps.cars.models import CarModel

from .filters import CarFilter
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    # def get_queryset(self):
    #     return car_filter(self.request.query_params.dict())


# class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer

class CarRetrieveUpdateDestroyView(GenericAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    def get(self, *args, **kwargs):
        car = self.get_object()
        print(car.auto_park.cars)
        return Response('ok')
