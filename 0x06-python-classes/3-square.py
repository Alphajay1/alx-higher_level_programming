#!/usr/bin/pythom3
"""Defines a square based on 2-square.py"""


class Square:
    """Represents a square

    Attributes:
        __size(int): size of one side of a square
    """
    def __init__(self, size=0):
        """Initialize the square

        Args:
            size(int): size of one side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        else:
            if size < 0:
                raise ValueError("size must be >= 0")

            else:
                self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return ((self.__size) ** 2)
