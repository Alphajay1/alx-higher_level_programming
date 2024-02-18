#!/usr/bin/python3
"""Contains the class 'MyList'"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
