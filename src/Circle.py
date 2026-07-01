from . import Figure


class Circle(Figure.Figure):
    __pi = 3.141592653589793

    def __init__(self, radius: int | float):
        if isinstance(radius, bool):
            raise TypeError("Expected int or float, not boolean")
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError(f"Radius must be int or float, got {type(radius)}")
        if radius <= 0:
            raise ValueError(f"Sides must be above zero, current is {radius}")
        self.radius = radius

    @property
    def area(self):
        return self.__pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * self.__pi * self.radius
