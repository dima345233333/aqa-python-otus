import pytest
from src.Square import Square



class TestSquare:
    def test_init(self):
        width = 1
        square = Square(width)
        assert isinstance(square, Square), "type is not Square"

    @pytest.mark.parametrize(
        "test_width",
        [0, -1, -100],
    )
    def test_negative_init(self, test_width):
        with pytest.raises(ValueError):
            square = Square(test_width)

    @pytest.mark.parametrize(
        ("test_width", "test_area"),
        [
            (1, 1),
            (2, 4),
            (5, 25),
            (100, 10000),
            (1.1, 1.21),
            (5.55, 30.8025),
        ],
    )
    def test_positive_area(self, test_width, test_area):
        square = Square(test_width)
        assert pytest.approx(square.area, rel=1e-5) == test_area, (
            f"Area must be {test_area}, actual is {square.area}"
        )

    @pytest.mark.parametrize(
        ("test_width", "test_perimeter"),
        [
            (1, 4),
            (2, 8),
            (5, 20),
            (100, 400),
            (1.1, 4.4),
            (5.55, 22.2),
        ],
    )
    def test_positive_perimeter(self, test_width, test_perimeter):
        square = Square(test_width)
        assert pytest.approx(square.perimeter, rel=1e-6) == test_perimeter, (
            f"Perimeter must be {test_perimeter}, actual is {square.perimeter}"
        )

    @pytest.mark.parametrize(
        "test_width",
        [True, "12", ([1, 1]), (1, 1)],
    )
    def test_negative_type(self, test_width):
        with pytest.raises(TypeError):
            square = Square(test_width)