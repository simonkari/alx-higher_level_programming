#!/usr/bin/python3
#!/usr/bin/python3
"""
A module that tests different behaviors of the Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """
    def setUp(self):
        self.square = Square(5)

    def test_pep8_square(self):
        """
        Test that checks PEP8 for Square class
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_getter(self):
        self.assertEqual(self.square.size, 5)

    def test_setter(self):
        self.square.size = 8
        self.assertEqual(self.square.size, 8)

    @unittest.expectedFailure
    def test_invalid_size(self, invalid_size):
        with self.assertRaises((TypeError, ValueError)):
            self.square.size = invalid_size

    def test_invalid_sizes(self):
        invalid_sizes = ["Hi", -5, 0, 1.5, (2, 8), '', None, [4, 7], {"hi": 5, "world": 8}]
        for size in invalid_sizes:
            with self.subTest(size=size):
                self.test_invalid_size(size)

    def test_width(self):
        self.square.size = 6
        self.assertEqual(self.square.width, 6)
        self.assertEqual(self.square.height, 6)

    def test_to_dictionary(self):
        Square._Base__nb_objects = 0

        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
       
