# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ErrorZero(Exception):

    def __init__(self) -> None:
        super().__init__('Деление на 0 недопустимо')


number = int(input('Введите делимое число  - '))


def div(number: int, divider: int) -> float:
    if divider == 0:
        raise ErrorZero()
    return round(number / divider, 2)


while (i := input('Введите делитель ')) != '':
    try:
        print(f'Частное {div(number, int(i))}')
    except ErrorZero as e:
        print(e)
        pass
