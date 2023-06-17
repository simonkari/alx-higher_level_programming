#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_property_with_integer(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_id_property_with_negative_integer(self):
        base = Base(-10)
        self.assertEqual(base.id, -10)

    def test_id_property_with_float(self):
        base = Base(2.15)
        self.assertEqual(base.id, 2.15)

    def test_id_property_without_argument(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_property_with_none(self):
        base = Base(None)
        self.assertEqual(base.id, 1)

    def test_id_property_with_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Base(6, 3)

    def test_private_attribute_access(self):
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

if __name__ == '__main__':
    unittest.main()
