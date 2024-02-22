#!/usr/bin/python3
"""
Contains the base class BaseGeometry and subclass Rectangle and Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
