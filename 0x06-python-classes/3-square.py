#!/usr/bin/pythom3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size(int): size of one side of a square
    """
    def __init__(self, size=0):
        """Initializes the square

        Args:
            size(int): size of one side of the square

        Returns:
            None
        """
        try:

            if type(size) is not int:
                raise TypeError("size must be an integer")

            else:

                if size < 0:
                    raise ValueError("size must be >= 0")

        except (TypeError, ValueError):

            raise
        self.__size = size

    def area(self):
        """Calculates the square's area
        
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
