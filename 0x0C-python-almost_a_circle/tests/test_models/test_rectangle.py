#!/usr/bin/python3
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rectangles = [
            Rectangle(10, 2),
            Rectangle(2, 10),
            Rectangle(10, 2, 0, 0, 12)
        ]

    def test_pep8_base(self):
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        r1 = self.rectangles[0]
        r2 = self.rectangles[1]
        r3 = self.rectangles[2]

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

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

    def test_type_param(self):
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)

        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)

        with self.assertRaises(TypeError):
            Rectangle('', 4)

        with self.assertRaises(TypeError):
            Rectangle(True, 4)

        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)

        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")

        with self.assertRaises(TypeError):
            Rectangle(5, False)

        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)

        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576398576)

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)

        # Add the missing line of code below:
        # raise TypeError()


if __name__ == '__main__':
    unittest.main()
