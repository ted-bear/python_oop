import random

class Animal:
    def __init__(self, a, w, s):
        self.age = a
        self.weight = w
        self.speed = s

    def foo(self):
        pass

    def run(self, new_speed) -> None:
        self.speed = new_speed

    def stop(self) -> None:
        self.speed = 0

class Cat(Animal):

    def __init__(self, n, a, w, s):
        super().__init__(a, w, s)
        self.name = n
        self.fq = 100

    def foo(self):
        print('Кошка мурлычет')

    def purr(self, freq):
        self.fq = freq


class Bird(Animal):

    def foo(self):
        print('Птица поет')

    def fly(self, new_speed):
        self.run(new_speed)


if __name__ == '__main__':
    animals = []

    for i in range(500):
        rand = random.Random()
        num = rand.randint(0, 1)
        if num == 0:
            animals.append(Cat("M", 1 ,1, 1))
        else:
            animals.append(Bird(1, 1, 1))

    for animal in animals:
        animal.foo()
