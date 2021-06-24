# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title='Запуск отрисовки'):
        self.title = title

    def draw(self):
        print(f'Набор для рисования {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Рисуем маркером {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()
