# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, name, color, speed, is_polise=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_polise = is_polise
        print(f'Модель -  {self.name} Цвет - {self.color} Cкорость - {self.speed} Полиция - {self.is_polise}')

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        print(f'{self.name} машина повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'{self.name} скорость автомобиля - {self.speed}')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False,):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        return f'{self.name} скорость автомобиля - {self.speed} - превышение скорости' \
            if self.speed > 60 else f'{self.name} скорость автомобиля - {self.speed}'


class SportCar(Car):

    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        return f'{self.name} скорость автомобиля - {self.speed} - превышение скорости \'' \
            if self.speed > 60 else f'{self.name} скорость автомобиля - {self.speed}'


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


towncar = TownCar('Автобус', 'Желтый', 70)
towncar.stop()

sportcar = SportCar('Феррари', 'красный', 350)
sportcar.go()

workcar = WorkCar('Зил', 'серый', 30)
workcar.turn(0)

police_car = PoliceCar('ДПС', 'Белый', 100)
police_car.turn(1)
