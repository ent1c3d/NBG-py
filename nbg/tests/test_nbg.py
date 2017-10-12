import unittest
import datetime
from nbg.nbg import Nbg


class TestNbg(unittest.TestCase):
    def setUp(self):
        self.nbg = Nbg('USD')

    def test_is_supported(self):
        self.assertTrue(Nbg.is_supported('USD'))
        self.assertFalse(Nbg.is_supported('USD2'))

    def test_validate(self):
        self.assertIsNone(Nbg.validate('USD'))
        with self.assertRaises(Exception):
            Nbg.validate('USD2')

    def test_get_currency_rate(self):
        self.assertIsInstance(float(Nbg.get_currency_rate('USD')), float)
        self.assertIsInstance(float(Nbg.get_currency_rate('RUB')), float)

        self.assertIsInstance(float(self.nbg.currency_rate), float)

    def test_get_description(self):
        self.assertIsInstance(Nbg.get_description('USD'), str)
        self.assertIsInstance(Nbg.get_description('RUB'), str)

        self.assertIsInstance(self.nbg.description, str)

    def test_get_change(self):
        self.assertIsInstance(float(Nbg.get_change('USD')), float)
        self.assertIsInstance(float(Nbg.get_change('RUB')), float)

        self.assertIsInstance(float(self.nbg.change), float)

    def test_get_rate(self):
        self.assertIn(Nbg.get_rate('USD'), (-1, 0, 1))
        self.assertIn(Nbg.get_rate('RUB'), (-1, 0, 1))

        self.assertIn(self.nbg.rate, (-1, 0, 1))

    def test_date(self):
        self.assertIsInstance(datetime.datetime.strptime(Nbg.get_date(), "%Y-%m-%d").date(), datetime.date)

        self.assertIsInstance(datetime.datetime.strptime(self.nbg.date, "%Y-%m-%d").date(), datetime.date)


if __name__ == '__main__':
    unittest.main()
