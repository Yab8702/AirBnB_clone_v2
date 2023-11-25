#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = State(name="Texas")

    def test_name(self):
        """ """
        self.assertEqual(type(self.new.name), str)
        self.assertEqual(self.new.name, "Texas")
