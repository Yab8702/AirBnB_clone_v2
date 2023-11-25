#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = Amenity(name="Wi-Fi")

    def test_name(self):
        """ """
        self.assertEqual(type(self.new.name), str)
        self.assertEqual(self.new.name, "Wi-Fi")
