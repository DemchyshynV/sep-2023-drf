from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None
