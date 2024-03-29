#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """
    A rectangle
    Args:
        width (int) : The width
        height (int): The height
    """
    def __init__(self, width=0, height=0):
        """Creates a new Rectangle instance"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a value for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets a value for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
