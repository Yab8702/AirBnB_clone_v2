#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = Review(place_id="123-756", user_id="790-543", text="Lorem")

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.new.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.new.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.new.text), str)
