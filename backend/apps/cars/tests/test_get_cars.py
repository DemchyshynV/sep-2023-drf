from unittest import TestCase
from unittest.mock import MagicMock, patch

from apps.cars.service import get_cars


class GetCarsTestCase(TestCase):
    @patch('apps.cars.service.requests.get')
    def test_status_code_not_200(self, mocked_requests_get:MagicMock):
        response = MagicMock(status_code=400)
        mocked_requests_get.return_value = response
        count = get_cars()

        self.assertEqual(count, 0)

    @patch('apps.cars.service.requests.get')
    def test_status_code__200(self, mocked_requests_get: MagicMock):
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = [{"brand":"BMW"}, {"brand":"Audi"}]
        mocked_requests_get.return_value = response
        count = get_cars()

        self.assertEqual(count, 2)

