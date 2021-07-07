# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Реализуйте механизм валидации вводимых пользователем данных.

class Stockroom:
    @staticmethod
    def get_stockroom_info():
        print(
            f'Склад ОРГ-1: площадь склада: 750 м2; высота: 8м; класс С;'
            f' склад собственный для хранения готовых товаров, отапливаемый.')

    def __init__(self):
        self.__stockroom = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStockroomError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__stockroom.extend(equipments)

    def transfer(self, item: int, department: str):
        if not isinstance(item, int):
            raise TransferStockroomError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__stockroom[item]

        if item.department:
            raise TransferStockroomError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__stockroom[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__stockroom[key]

    def __iter__(self):
        return self.__stockroom.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__stockroom)} устройств"


class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStockroomError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStockroomError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStockroomError = AcceptStockroomError


class ValidateEquipmentError(AppError):
    pass


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    stockroom = Stockroom()
    Stockroom.get_stockroom_info()
    stockroom.add(Printer.create(4, vendor="Epson", model="XP-400"))
    stockroom.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    stockroom.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    stockroom.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(stockroom)

    for idx, itm in stockroom.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"Резервируем {itm} в 'Отдел ЯФ'")
        stockroom.transfer(idx, 'Отдел ЯФ')

    for idx, itm in stockroom.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(stockroom)
    print("Списываем 1 устройство")
    del stockroom[0]
    print(stockroom)
