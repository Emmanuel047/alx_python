class Square:
    def __init__(self, size):
        self.__size = size
    
    def area(self):
        return self.__size ** 2

# Instantiate the Square class
square1 = Square(5)
print("Area of square1:", square1.area())  # Output: Area of square1: 25

square2 = Square(7)
print("Area of square2:", square2.area())  # Output: Area of square2: 49
