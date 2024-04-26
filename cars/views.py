from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarModel


# class CarTestView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         params_dict = self.request.query_params.dict()
#         print(params_dict)
#         print(data)
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
# class CarDetailView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('hello from get')


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [{'id': car.pk, 'brand': car.brand, 'price': car.price, 'year':car.year} for car in cars]
        return Response(res)

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        CarModel.objects.create(**data)
        return Response('created')
