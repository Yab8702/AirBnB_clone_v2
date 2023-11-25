#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.new = User(first_name="Mohammed", last_name="Khalil",
                        email="example@coding.com", password="mlmlml")

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.new.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.new.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.new.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.new.password), str)
