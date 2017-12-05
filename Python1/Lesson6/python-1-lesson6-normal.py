# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # атаковать противника
    def attack(self, armor):
        enemy_force = armor.damage
        print("{} наносит удар.".format(self.name))
        self._damage(enemy_force)

    # посчитать урон
    def _damage(self, enemy_force):
        damage = enemy_force - self.armor
        print("{} получает {} урона.".format(self.name, damage))
        self.health -= damage


class Player(Person):
    # увернуться
    def dodge(self):
        if random.choice([False, True]):
            print("'{}' уварачивается от удара.".format(self.name))
            return True
        return False

    # посчитать урон
    def _damage(self, enemy_force):
        # если увернулся, то не получил урона
        if self.dodge():
            damage = 0
            return

        damage = enemy_force - self.armor
        print("{} получает {} урона.".format(self.name, damage))
        self.health -= damage

    def get_health(self):
        return self.health

class Enemy(Person):
    pass


class Battle():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def play(self):
        while not self.battle_over():
            self.player.attack(self.enemy)
            if not self.battle_over():
                self.enemy.attack(self.player)
            else:
                break

    def battle_over(self):
        if self.player.get_health() > 0 and self.enemy.get_health() <= 0:
            print("Битва окончена. победил '{}'".format(self.player.name))
            return True
        elif self.enemy.get_health() > 0 and self.player.get_health() <= 0:
            print("Битва окончена. победил '{}'".format(self.enemy.name))
            return True
        return False


player = Player("добрый рыцарь", 150, 35, 12)
armor = Player("злой гоблин", 210, 43, 17)

game = Battle(player, armor)
game.play()
