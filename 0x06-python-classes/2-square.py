#!/usr/bin/python3
"""Define a square class based on  1-square.py)"""


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

        if type(size) is not int:
            raise TypeError("size must be an integer")

        else:
            if size < 0:
                raise ValueError("size must be >= 0")

            else:
                self.__size = size
