#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""

class Rectangle:
    """
       An empty Rectangle class
    """
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):

        """
               Checks the parameters and initializes some values
               Args:
                   width (:obj:`int`, optional): The width of the Rectangle.
                   height (:obj:`int`, optional): The height of the Rectangle.
        """
        self.width = width
        self.height = height
    @property
    def width(self):
                    """
                    return the width
                    """
                    return self.__width
    @width.setter
    def width(self, value):
        """
                Args:
                set the parameter height which is value
                raises:
                TypeError("height must be an integer") if type (height) is not int
                ValueError("height must be >= 0") if width < 0
        """

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
        set the parameter height which is value
        raises:
        TypeError("height must be an integer") if type (height) is not int
        ValueError("height must be >= 0") if width < 0
        """
        if type(self.__height) is not int:
            raise TypeError("width must be an integer")
        elif self.__height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

