'''
Square class
'''

class Square:

    def __init__(self, size = 0):

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.size = int(size)

my_square = Square(9)
my_square.__size()