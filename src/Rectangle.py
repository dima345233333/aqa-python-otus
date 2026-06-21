import Figure


class Rectangle(Figure.Figure):
    def __init__(self, width: int | float, height: int | float):
        if isinstance(width, bool) or isinstance(height, bool):
            raise TypeError("Expected int or float, not boolean")
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError(f"Width must be int or float, got {type(width)}")
        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError(f"Height must be int or float, got {type(height)}")
        if width <= 0 or height <= 0:
            raise ValueError(f"Sides must be above zero, current is {width}x{height}")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
