# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'


employee_1 = Position('Олег', 'Иванов', 'Директор', 80000, 40000)
print(f'{employee_1.get_full_name()}, {employee_1.position}, {employee_1.get_full_profit()}')

employee_2 = Position('Федор', 'Петров', 'Товаровед', 40000, 15000)
print(f'{employee_2.get_full_name()}, {employee_2.position}, {employee_2.get_full_profit()}')

employee_3 = Position('Василий', 'Сидоров', 'Кассир', 20000, 5000)
print(f'{employee_3.get_full_name()}, {employee_3.position}, {employee_3.get_full_profit()}')
