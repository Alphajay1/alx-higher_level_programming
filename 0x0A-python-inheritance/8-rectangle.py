#!/usr/bin/python3
"""
Contains class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a Rectangle"""
    def __init__(self, width, height):
        """Initializes the Rectangle"""
        self.__width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
