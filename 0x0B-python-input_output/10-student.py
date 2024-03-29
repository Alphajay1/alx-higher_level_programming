#!/usr/bin/python3
"""
contains a class "Student"
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): The first name of a student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved

        Otherwise, all attributes must be retrieved

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
