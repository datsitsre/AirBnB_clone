import models
import unittest
from datetime import datetime


class CityTest(unittest.TestCase):
    """tests for the class City"""

    def test_documentation(self):
        """tests module and class docstring"""
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(models.city.City.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.city.City()
        self.assertIsInstance(instance, models.city.City)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.city.City()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
