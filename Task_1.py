# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division():
    try:
        div_1 = float(input('Введите первое число  - '))  # Делимое
        div_2 = float(input('Введите второе число  - '))  # Делитель
        return div_1 / div_2
    except ZeroDivisionError:
        return 'None'


result = division()
print(f'{result:.2}')
