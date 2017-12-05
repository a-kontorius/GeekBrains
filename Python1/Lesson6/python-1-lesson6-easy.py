# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass


class SportCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass


class WorkCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass


class PoliceCar():
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)
        self.cabin_themperature = 20

    def turn_on_air_conditioner(self):
        self.cabin_themperature -= 5


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, is_police)

    def accelerate(self):
        self.speed += 10

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, True)
        self.cargo = False

    def load_cargo(self):
        self.cargo = True

    def unload_cargo(self):
        self.cargo = False


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name, True)
        self.siren = False

    def turn_on_siren(self):
        self.siren = True

    def turn_off_siren(self):
        self.siren = False
