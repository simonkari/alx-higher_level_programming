#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 2 - 13"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(attr))
        if value <= 0 and attr in ['width', 'height']:
            raise ValueError('{} must be > 0'.format(attr))
        elif value < 0 and attr in ['x', 'y']:
            raise ValueError('{} must be >= 0'.format(attr))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__integer_validator('y', value)
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        display = '\n' * self.y
        display += '\n'.join(' ' * self.x + '#' * self.width for _ in range(self.height))
        print(display)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if attr == 'id':
                    self.id = value
                    Base._Base__assigned_ids.add(value)
                else:
                    setattr
