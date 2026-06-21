from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure: Figure):
        if not isinstance(figure, Figure):
            raise TypeError("figure must be an instance of Figure")
        return self.area + figure.area
