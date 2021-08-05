class Shape:
    pass


class Circle(Shape):

    def draw(self):
        print("Draw a circle")


class Square(Shape):

    def draw(self):
        print("Draw a Square")


class Rectangle(Shape):

    def draw(self):
        print("Draw a Rectangle")


class ShapeFactory:

    @classmethod
    def create(cls, shape="circle"):
        if shape == "circle":
            return Circle()
        if shape == "square":
            return Square()
        if shape == "rectangle":
            return Rectangle()


c1 = ShapeFactory.create("square")
c1.draw()

