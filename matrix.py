# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

import numpy
import random

matrix_1 = numpy.zeros((4, 4))
for i in range(4):
    for j in range(4):
        matrix_1[i][j] = random.randint(0, 9)

matrix_2 = numpy.zeros((4, 4))
for i in range(4):
    for j in range(4):
        matrix_2[i][j] = random.randint(0, 9)


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        return self.matrix + other.matrix


mat_1 = Matrix(matrix_1)
mat_2 = Matrix(matrix_2)
print(mat_1)
print(mat_2)
print(mat_1 + mat_2)
