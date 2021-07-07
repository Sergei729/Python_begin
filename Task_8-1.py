# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:

    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def convert(cls, data):
        enter_date = []

        for i in data.split():
            if i != '-':
                enter_date.append(i)

        return int(enter_date[0]), int(enter_date[1]), int(enter_date[2])

    @staticmethod
    def check(day, month, year):
        data_check = []

        if 1 > day or day > 31:
            data_check.append(f'Неверная дата, день не существует')
        if 1 > month or month > 12:
            data_check.append(f'Неверная дата, месяц не существует')
        if 0 >= year:
            data_check.append(f'Неверная дата, год не существует')
        if len(data_check) > 0:
            return " ".join(data_check)
        else:
            return f'Введены верные значения даты.'

    def __str__(self):
        return f'Текущая дата - {Data.convert(self.data)}'


today = Data('11 - 1 - 2001')
print(today)

print(Data.check(45, 5, 2018))
print(today.check(25, 5, 2018))

print(Data.check(11, 14, 2022))
print(today.check(11, 12, 2022))

print(Data.check(11, 11, -8))
print(today.check(30, 1, 2008))

print(Data.convert('16 - 16 - 3'))
print(today.convert('07 - 07 - 2021'))
