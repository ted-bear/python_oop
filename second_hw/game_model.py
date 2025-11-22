# Моделирование сущностей из игры Сталкер

class Stalker:

    def __init__(self, name, age, group, hp, irradiation):
        self.__name = name
        self.__age = age
        self.__weapon = None  # Текущее оружие
        self.__group = group  # Группировка: 0 - вольный, 1 - бандит, 2 - военный
        self.__hp = hp  # Уровень здоровья
        self.__irradiation = irradiation  # Текущий уровень облучения радиацией

    def Take_Antidote(self):
        self.__irradiation = 0

    def Take_Medicine(self):
        self.__hp = 100

    def Take_Riffle(self, riffle):
        self.__weapon = riffle

    def Attack(self):
        if self.__weapon is None:
            print('You do not have weapon')
            return
        self.__weapon.Shoot()


class Weapon:

    def __init__(self, name, damage, ammunition, state):
        self.__name = name
        self.__damage = damage
        self.__ammunition = ammunition
        self.__state = state  # Состояние оружия: 0 - новое, 1 - поцарапанное, 2 - поношенное, 3 - сломанное

    def Shoot(self):
        if self.__ammunition <= 0:
            print(f'Gun {self.__name} is empty')
        print(f'Gun {self.__name} is shooting')
        self.__ammunition -= 1

    def Reload(self):
        self.__ammunition = 30

    def Break_Down(self):
        self.__state += 1
        print(f'Gun {self.__name} is breaking down, new state: {self.__state}')


class Artifact:

    def __init__(self, name, hp, irradiation, psi_level, price):
        self.__name = name
        self.__hp = hp  # Количество жизней, которые увеличиваются или восстанавливаются
        self.__irradiation = irradiation  # Количество радиации, которое артефакт излучает или поглащает
        self.__psi_level = psi_level  # Количество пси-изучения, которое артефакт излучает или поглащает
        self.__price = price  # цена артефакта

    def influence_health(self, hp):
        hp += self.__hp

    def influence_irradiation(self, irradiation):
        irradiation += self.__irradiation

    def influence_psi_level(self, psi):
        psi += self.__psi_level
