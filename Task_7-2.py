# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.size / 6.5) + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return round(2 * self.size + 0.3) / 100


coat = Coat(int(input('Введите размер для пальто V = ')))
suit = Suit(int(input('Введите рост для костюма H = ')))
print(coat + suit)
