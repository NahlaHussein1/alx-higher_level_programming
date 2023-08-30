reating a square class """


class Square:
    """ Defining a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: size of the square
         """
        self.__size = size

    @property
    def size(self):
        """ Getting the size of the square "
