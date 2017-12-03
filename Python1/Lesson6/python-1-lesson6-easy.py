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
