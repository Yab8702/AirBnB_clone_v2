#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = City(name="Errachidia", state_id="65f-9d3")

    def test_name(self):
        """ """
        self.assertEqual(type(self.new.name), str)
        self.assertEqual(self.new.name, "Errachidia")

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.new.state_id), str)
        self.assertEqual(self.new.state_id, "65f-9d3")
