# Моделирование сущностей из игры Сталкер

class Stalker:
    
    def __init__(self, name, age, group, hp, irradiation):
        self.name = name
        self.age = age
        self.weapon = None # Текущее оружие
        self.group = group # Группировка: 0 - вольный, 1 - бандит, 2 - военный
        self.hp = hp # Уровень здоровья
        self.irradiation = irradiation # Текущий уровень облучения радиацией

    def Take_Antidote(self):
        self.irradiation = 0

    def Take_Medicine(self):
        self.hp = 100

    def Take_Riffle(self, riffle):
        self.weapon = riffle

    def Attack(self):
        if self.weapon == None:
            print('You do not have weapon')
            return
        self.weapon.Shoot()

class Weapon:

    def __init__(self, name, damage, ammunition, state):
        self.name = name
        self.damage = damage
        self.ammunition = ammunition
        self.state = state # Состояние оружия: 0 - новое, 1 - поцарапанное, 2 - поношенное, 3 - сломанное

    def Shoot(self):
        if self.ammunition <= 0:
            print(f'Gun {self.name} is empty')
        print(f'Gun {self.name} is shooting')
        self.ammunition -= 1

    def Reload(self):
        self.ammunition = 30

    def Break_Down(self):
        self.stat += 1
        print(f'Gun {self.name} is breaking down, new state: {self.state}')


class Artifact:

    def __init__(self, name, hp, irradiation, psi_level, price):
        self.name = name
        self.hp = hp # Количество жизней, которые увеличиваются или восстанавливаются
        self.irradiation = irradiation # Количество радиации, которое артефакт излучает или поглащает
        self.psi_level = psi_level # Количество пси-изучения, которое артефакт излучает или поглащает
        self.price = price # цена артефакта

    def influence_health(self, hp):
        hp += self.hp
    
    def influence_irradiation(self, irradiation):
        irradiation += self.irradiation

    def influence_psi_level(self, psi):
        psi += self.psi_level
