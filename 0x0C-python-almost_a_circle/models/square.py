#!/usr/bin/python3
#!/usr/bin/python3
""" Program that defines a Square based on Rectangle """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieve the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Override the __str__ method to return a custom string """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute using positional and keyword arguments """
        attribute_list = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_list):
                    setattr(self, attribute_list[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
