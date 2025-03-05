class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        area = self.__side_length * self.__side_length
        return f'The area of the square is {area}'

    def info(self):
        return f'Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}'


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        area = self.__length * self.__width
        return f'The area of the rectangle is {area}'

    def info(self):
        return f'The Rectangle length: {self.__length}, width: {self.__width},  area: {self.calculate_area()}.'




total_area = [Square(4), Square(8), Rectangle(6, 4), Rectangle(5, 4), Rectangle(8, 4)]


for i in total_area:
    print(i.info())
