#!/usr/bin/python3

"""Unittests for console

Test Classes:
    TestOrdinaryCommands
    TestCreateCommand
    TestShowCommand
    TestDestroyCommand
"""

import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestOrdinaryCommands(unittest.TestCase):
    """
    Unittests the typical console commands
    """

    def test_quit(self):
        '''Test the `quit` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('quit')
            output = f.getvalue()
            self.assertEqual(output, '')

    def test_EOF(self):
        '''Test the `EOF` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('EOF')
            output = f.getvalue()
            self.assertEqual(output, '\n')

    def test_help(self):
        '''Test the `help` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            output = f.getvalue().strip()
            self.assertEqual(output, HBNBCommand.do_quit.__doc__)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help EOF')
            output = f.getvalue().strip().strip()
            self.assertEqual(output, HBNBCommand.do_EOF.__doc__)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help help')
            output = f.getvalue().strip()
            self.assertEqual(output, HBNBCommand.do_help.__doc__)

    def test_emptyline(self):
        '''Test empty command line'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('')
            output = f.getvalue()
            self.assertEqual(output, '')


class TestCreateCommand(unittest.TestCase):
    """
    Unittests the `create` command
    """

    def setUp(self):
        '''Runs before every test'''
        from models import storage

        self.storage = storage
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._FileStorage__objects = {}

        self.arizona = State(name='Arizona')
        self.arizona.save()

        self.san_jose = City(name='San Jose', state_id=self.arizona.id)
        self.san_jose.save()

        self.john_doe = User(email='john_doe@baz.com', password='mlmlml',
                             first_name='John', last_name='Doe')
        self.john_doe.save()

        self.huge_house = Place(name='Huge House', description='Sweet home',
                                city_id=self.san_jose.id,
                                user_id=self.john_doe.id)
        self.huge_house.save()

        self.john_review = Review(text='Excellent', user_id=self.john_doe.id,
                                  place_id=self.huge_house.id)
        self.john_review.save()

        self.heating = Amenity(name='Heating')
        self.heating.save()

    def tearDown(self):
        '''Runs after each test'''

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `create` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Using DBStorage')
    def test_create_BaseModel(self):
        '''Test creating a BaseModel instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'BaseModel.{output_id}', objs_dict.keys())

    def test_create_User(self):
        '''Test creating a User instance with '''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User email="OmarYoussef@ex.com" ' +
                                 'password="mlml" age=22 height=1.7 nil=mess')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()
            key = f'User.{output_id}'

            self.assertIn(key, objs_dict.keys())

            user = objs_dict[key]

            self.assertEqual(user.email, 'OmarYoussef@ex.com')
            self.assertEqual(user.password, 'mlml')
            if os.getenv('HBNB_TYPE_STORAGE') != 'db':
                self.assertEqual(user.age, 22)
                self.assertEqual(user.height, 1.7)

    def test_create_State(self):
        '''Test creating a State instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Arizona"')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            key = f'State.{output_id}'

            self.assertIn(key, objs_dict.keys())
            self.assertEqual(objs_dict[key].name, 'Arizona')

    def test_create_City(self):
        '''Test creating a City instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="New_York" ' +
                                 f'state_id="{self.arizona.id}"')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            key = f'City.{output_id}'

            self.assertIn(key, objs_dict.keys())
            self.assertEqual(objs_dict[key].name, 'New York')
            self.assertEqual(objs_dict[key].state_id, self.arizona.id)

    def test_create_Place(self):
        '''Test creating a Place instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = 'create Place name="Home" description="Sweet" '
            cmd += f'user_id="{self.john_doe.id}" city_id="{self.san_jose.id}"'
            HBNBCommand().onecmd(cmd)
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Place.{output_id}', objs_dict.keys())

    def test_create_Amenity(self):
        '''Test creating a Amenity instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity name="Wi-Fi"')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Amenity.{output_id}', objs_dict.keys())

    def test_create_Review(self):
        '''Test creating a Review instance'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review text="Good" ' +
                                 f'user_id="{self.john_doe.id}" ' +
                                 f'place_id="{self.huge_house.id}"')
            output_id = f.getvalue().strip()
            objs_dict = self.storage.all()

            self.assertIn(f'Review.{output_id}', objs_dict.keys())


class TestShowCommand(unittest.TestCase):
    """
    Unittests the `show` command
    """

    def setUp(self):
        '''Runs before every test'''
        from models import storage

        self.storage = storage
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._FileStorage__objects = {}

        self.arizona = State(name='Arizona')
        self.arizona.save()

    def tearDown(self):
        '''Runs after each test'''

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `show` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Review')
            output = f.getvalue().strip()

            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show City d6586de3-e13b-4553-be56-2ebdb3')
            output = f.getvalue().strip()

            self.assertEqual(output, '** no instance found **')

    def test_show_an_instance(self):
        '''Test showing an instance, ex : State'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {self.arizona.id}')
            output = f.getvalue().strip()

            self.assertEqual(output, str(self.arizona))


class TestDestroyCommand(unittest.TestCase):
    """
    Unittests the `destroy` command
    """

    def setUp(self):
        '''Runs before every test'''
        from models import storage

        self.storage = storage
        storage.reload()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._FileStorage__objects = {}

    def tearDown(self):
        '''Runs after each test'''

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.storage._Filestorage__objects = {}

    def test_errors(self):
        '''Test Errors mangement of `destroy` command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Country')
            output = f.getvalue().strip()

            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Review')
            output = f.getvalue().strip()

            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy City d6586de3-e13b-4553-be56-2ebdb3')
            output = f.getvalue().strip()

            self.assertEqual(output, '** no instance found **')

    def test_destroy_an_instance(self):
        '''Test destroying an instance, ex : User'''

        user_m = User(email="example@gmail.com", password="mlmlml")
        user_m.save()
        objs_dict = self.storage.all()

        self.assertIn(f'User.{user_m.id}', objs_dict.keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy User {user_m.id}')
            output = f.getvalue().strip()

            objs_dict = self.storage.all()

            self.assertNotIn(f'User.{user_m.id}', objs_dict.keys())
