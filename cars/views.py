from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarModel
from .serializers import CarSerializer
from rest_framework import status

# Create
# Read/Retrieve
# Update
# Delete/Destroy
class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        # res = [{'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            # return Response('not found', status.HTTP_404_NOT_FOUND)
            raise Http404()
        # car_res = {'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year}
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car, data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        # for key, value in data.items():
        #     setattr(car, key, value)
        # brand = data['brand']
        # price = data['price']
        # year = data['year']
        # car.brand = brand
        # car.price = price
        # car.year = year

        # car.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            CarModel.objects.get(pk=pk).delete()
            # car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response(status=status.HTTP_204_NO_CONTENT)
