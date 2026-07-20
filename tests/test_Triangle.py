import pytest
from src.Triangle import Triangle


class TestTriangle:
    def test_init(self):
        side_1,side_2,side_3 = 3, 4, 5
        triangle = Triangle(side_1,side_2,side_3)
        assert isinstance(triangle, Triangle), "type is not Triangle"

    @pytest.mark.parametrize(
        ("test_side_1", "test_side_2", "test_side_3"),
        [(0,1,2), (-1,1,2), (1,2,3)],
    )
    def test_negative_init(self, test_side_1, test_side_2,test_side_3):
        with pytest.raises(ValueError):
            triangle = Triangle(test_side_1, test_side_2,test_side_3)

    @pytest.mark.parametrize(
        ("test_side_1", "test_side_2", "test_side_3", "test_area"),
        [
            (4, 4, 4,6.928),
            (2.5, 3.5, 4.5,4.353),
            (100, 100, 100,4330.127),
        ],
    )
    def test_positive_area(self, test_side_1, test_side_2, test_side_3, test_area):
        triangle = Triangle(test_side_1, test_side_2, test_side_3)
        actual_area = round(triangle.area.real, 3)
        assert pytest.approx(actual_area, rel=1e-5) == test_area, (
            f"Area must be {test_area}, actual is {actual_area}"
        )

    @pytest.mark.parametrize(
        ("test_side_1", "test_side_2", "test_side_3", "test_perimeter"),
        [
            (4, 4, 4, 12),
            (2.5, 3.5, 4.5, 10.5),
            (100, 100, 100, 300),
        ],
    )
    def test_positive_perimeter(self, test_side_1, test_side_2, test_side_3, test_perimeter):
        triangle = Triangle(test_side_1, test_side_2, test_side_3)
        assert pytest.approx(triangle.perimeter, rel=1e-6) == test_perimeter, (
            f"Perimeter must be {test_perimeter}, actual is {triangle.perimeter}"
        )

    @pytest.mark.parametrize(
        ("test_side_1", "test_side_2", "test_side_3"),
        [(True, 1,1), ("12", 2,1), ([1,1], 2,2), ((1,1), 2,2)],
    )
    def test_negative_type(self, test_side_1, test_side_2,test_side_3):
        with pytest.raises(TypeError):
            rectangle = Triangle(test_side_1, test_side_2, test_side_3)
        with pytest.raises(TypeError):
            rectangle = Triangle(test_side_3, test_side_1, test_side_2)
        with pytest.raises(TypeError):
            rectangle = Triangle(test_side_2, test_side_3, test_side_1)
