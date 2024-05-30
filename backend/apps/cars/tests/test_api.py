from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.cars.models import CarModel

UserModel = get_user_model()


class CarAPITestCase(APITestCase):
    def setUp(self):
        self.car = CarModel.objects.create(brand='Audi', price=2000, year=2000)
        self.sample_car = {
            "brand": "Audi",
            "year": 2010,
            "price": 20000,
        }

    def _authenticate(self):
        email = 'admin@gmail.com'
        password = 'P@$$word1'
        response = self.client.post(reverse('users_list_create'), data={
            'email': email,
            'password': password,
            'profile': {
                "name": "Max",
                "surname": "Popov",
                "age": 15
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        response = self.client.post(reverse('auth_login'), {'email': email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_get_list_cars_without_auth(self):
        count = CarModel.objects.count()
        res = self.client.get(reverse('car_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(count, len(res.data))

    def test_create_car_without_auth(self):
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('car_list_create'), data=self.sample_car)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(count_before, CarModel.objects.count())

    def test_create_car_with_auth(self):
        self._authenticate()
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('car_list_create'), data=self.sample_car)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_before + 1, CarModel.objects.count())
