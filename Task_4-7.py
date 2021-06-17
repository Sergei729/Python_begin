# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.

from itertools import count
from math import factorial


def fact_gen(number):
    f_num = 1
    if number == 0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact_gen(int(input('Factorial number: '))):
    print(el)
