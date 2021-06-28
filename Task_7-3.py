# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

def make_order(rows, nums):
    return '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print('операция невозможна')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    def __str__(self):
        return f'{self.cells}'


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(make_order(3, 24))
