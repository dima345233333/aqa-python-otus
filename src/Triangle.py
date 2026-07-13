from cmath import sqrt

from . import Figure


class Triangle(Figure.Figure):
    def __init__(self, a: int | float, b: int | float, c: int | float):
        sides = [a, b, c]
        for side in sides:
            if isinstance(side, bool):
                raise TypeError("Expected int or float, not boolean")
            if not isinstance(side, int) and not isinstance(side, float):
                raise TypeError(f"Side must be int or float, got {type(side)}")
            if side <= 0:
                raise ValueError(f"Side must be > 0, got {side}")
        if not ((a + b > c) and (a + c > b) and (b + c > a)):
            raise ValueError(f"Triangle cannot exist with sides {a}x{b}x{c}")
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        self.__h = self.perimeter / 2
        return sqrt(
            self.__h * (self.__h - self.a) * (self.__h - self.b) * (self.__h - self.c)
        )

    @property
    def perimeter(self):
        return self.a + self.b + self.c
