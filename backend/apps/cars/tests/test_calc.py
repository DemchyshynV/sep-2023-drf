from unittest import TestCase

from apps.cars.service import calc


class CalcTestCase(TestCase):
    def test_plus(self):
        res = calc(1, 2, "+")
        self.assertEqual(res, 3)

    def test_minus(self):
        res = calc(1, 2, "-")
        self.assertEqual(res, -1)

    def test_multi(self):
        res = calc(1, 2, "*")
        self.assertEqual(res, 2)
