import pytest
from src.Rectangle import Rectangle


class TestRectangle:
    def test_init(self):
        width = 1
        height = 1
        rectangle = Rectangle(width,height)
        assert isinstance(rectangle, Rectangle), "type is not Rectangle"

    @pytest.mark.parametrize(
        ("test_width", "test_height"),
        [(0,0), (-1,1), (1,-1)],
    )
    def test_negative_init(self, test_width, test_height):
        with pytest.raises(ValueError):
            rectangle = Rectangle(test_width,test_height)

    @pytest.mark.parametrize(
        ("test_width", "test_height", "test_area"),
        [
            (1, 1, 1),
            (2, 1, 2),
            (1, 2, 2),
            (100, 101, 10100),
            (1.1, 1.2, 1.32),
            (5.55, 7.777, 43.16235),
        ],
    )
    def test_positive_area(self, test_width, test_height, test_area):
        rectangle = Rectangle(test_width,test_height)
        assert pytest.approx(rectangle.area, rel=1e-5) == test_area, (
            f"Area must be {test_area}, actual is {rectangle.area}"
        )

    @pytest.mark.parametrize(
        ("test_width", "test_height", "test_perimeter"),
        [
            (1, 1, 4),
            (2, 1, 6),
            (1, 2, 6),
            (100, 101, 402),
            (1.1, 1.2, 4.6),
            (5.55, 7.777, 26.654),
        ],
    )
    def test_positive_perimeter(self, test_width, test_height, test_perimeter):
        rectangle = Rectangle(test_width,test_height)
        assert pytest.approx(rectangle.perimeter, rel=1e-6) == test_perimeter, (
            f"Perimeter must be {test_perimeter}, actual is {rectangle.perimeter}"
        )

    @pytest.mark.parametrize(
        ("test_width", "test_height"),
        [(True, 1), ("12", 2), ([1,1], 2), ((1,1), 2)],
    )
    def test_negative_type(self, test_width, test_height):
        with pytest.raises(TypeError):
            rectangle = Rectangle(test_width, test_height)
        with pytest.raises(TypeError):
            rectangle = Rectangle(test_height, test_width)
