#!/usr/bin/python3
"""Defines a class Square based on 0-square.py by
Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """Defines a square

    Attributes:
        __size(int): size of one side of the square
    """

    def __init__(self, size):
        """Initializes a square

        Args:
            size(int): size of one side of a square

        Returns: None
        """

        self.__size = size
