from abc import  ABC , abstractmethod

class Shape(ABC):
    def __init__(self,color):
        self.color = color


    def show(self):
        pass


class Circle(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)

class Square(Shape):
    def show(self):
        self.color.paint(self.__class__.__name__)


class Color(ABC):
    def paint(self,shape):
        pass

class Red(Color):
    def paint(self,shape):
        print(f'Red color: {shape}')

class Blue(Color):
    def paint(self,shape):
        print(f'Blue color: {shape}')


blue = Blue()
circle = Circle(blue)
circle.show()

