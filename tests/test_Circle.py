import pytest
from src.Circle import Circle


class TestCircle:
    def test_init(self):
        radius = 1
        circle = Circle(radius)
        assert isinstance(circle, Circle), "type is not Circle"

    @pytest.mark.parametrize(
        "test_radius",
        [0, (-1), (-100)],
    )
    def test_negative_init(self, test_radius):
        with pytest.raises(ValueError):
            circle = Circle(test_radius)

    @pytest.mark.parametrize(
        ("test_radius", "area"),
        [
            (1, 3.141593),
            (2, 12.566371),
            (5, 78.539816),
            (100, 31415.926536),
            (1.1, 3.801327),
            (5.55, 96.768908),
            (7.77777, 190.046583),
        ],
    )
    def test_positive_area(self, test_radius, area):
        circle = Circle(test_radius)
        assert pytest.approx(circle.area, rel=1e-6) == area, (
            f"Area must be {area}, actual is {circle.area}"
        )

    @pytest.mark.parametrize(
        ("test_radius", "perimeter"),
        [
            (1, 6.283185),
            (2, 12.566370),
            (5, 31.415926),
            (100, 628.318530),
            (1.1, 6.911503),
            (5.55, 34.871678),
            (7.77777, 48.869170),
        ],
    )
    def test_positive_perimeter(self, test_radius, perimeter):
        circle = Circle(test_radius)
        assert pytest.approx(circle.perimeter, rel=1e-6) == perimeter, (
            f"Perimeter must be {perimeter}, actual is {circle.perimeter}"
        )

    @pytest.mark.parametrize(
        "test_type",
        ["123", ([1, 2]), (1, 2), True],
    )
    def test_negative_type(self, test_type):
        with pytest.raises(TypeError):
            circle = Circle(test_type)
