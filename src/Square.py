from . import Rectangle


class Square(Rectangle.Rectangle):
    def __init__(self, x: int | float):
        if x <= 0:
            raise ValueError(f"Side must be above zero, current is {x}")
        super().__init__(x, x)
