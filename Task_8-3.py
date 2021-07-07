# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumber(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []
    while True:
        number = input('Введите последовательность чисел: ')

        if number == 'q':
            break
        try:
            if not number.isdigit():
                raise NotNumber(f"'{number}' - неверный тип данных")
            my_list.append(int(number))
        except NotNumber as e:
            print(e)
    print(f' Введенные данные {my_list}')
