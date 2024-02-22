#!/usr/bin/python3
"""
Contains class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """Contains public instance method 'area' and 'integer_validator'"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a Rectangle"""
    def __init__(self, width, height):
        """Initializes the Rectangle"""
        self.__width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
