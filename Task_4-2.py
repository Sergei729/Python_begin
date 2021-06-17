# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

my_list = [random.randint(0, 1000) for i in range(15)]
print(my_list)


new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(new_list)
