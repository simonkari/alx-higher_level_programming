#!/usr/bin/python3
#!/usr/bin/python3
"""
A module that tests different behaviors
of the Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class
        """
        cls.syntax = pep8.StyleGuide(quit=True)
        cls.check = cls.syntax.check_files(['models/rectangle.py'])

    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        self.assertEqual(
            self.check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherits from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        self.assertRaises(TypeError, Rectangle)

    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        self.assertRaises(TypeError, Rectangle, 'Monty', 'Python')

    def test_type_param(self):
        """
        Test different types of parameters
        for a Rectangle class
        """
        self.assertRaises(TypeError, Rectangle, 1.01, 3)
        self.assertRaises(ValueError, Rectangle, -234234242, 45)
        self.assertRaises(TypeError, Rectangle, '', 4)
        self.assertRaises(TypeError, Rectangle, True, 4)
        self.assertRaises(TypeError, Rectangle, 5, 1.76)
        self.assertRaises(TypeError, Rectangle, 5, "Hello")
        self.assertRaises(TypeError, Rectangle, 5, False)
        self.assertRaises(ValueError, Rectangle, 5, -4798576398576)
        self.assertRaises(TypeError, Rectangle, 5, 1, 1.50)
        self.assertRaises(TypeError, Rectangle, 5, 6, "test")
        self.assertRaises(TypeError, Rectangle, 5, 7, False)
        self.assertRaises(ValueError, Rectangle, 5, 7, -4798576398576)
        self.assertRaises(TypeError, Rectangle, 5, 1, 1, 1.53)
        self.assertRaises(TypeError, Rectangle, 5, 6, 5, "test")
        self.assertRaises(TypeError, Rectangle, 5, 7, 7, False)
        self.assertRaises(ValueError, Rectangle, 5, 9, 5, -4798576398576)


if __name__ == '__main__':
    unittest.main()
