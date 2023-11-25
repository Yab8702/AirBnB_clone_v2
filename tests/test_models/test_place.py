#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = Place(city_id='987-656', user_id='6f4-96c', name='Yard',
                         description='Nice Yard', number_rooms=2,
                         number_bathrooms=1, max_guest=3, price_by_night=20.9,
                         longitude=88.4, latitude=137.3)

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.new.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.new.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.new.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.new.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.new.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.new.price_by_night), float)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.new.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.new.latitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.new.amenity_ids), list)
