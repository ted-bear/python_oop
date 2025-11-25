class Animal:
    def __init__(self, a, w, s):
        self.age = a
        self.weight = w
        self.speed = s

    def run(self, new_speed) -> None:
        self.speed = new_speed

    def stop(self) -> None:
        self.speed = 0

class Cat(Animal):

    def __init__(self, n, a, w, s):
        super().__init__(a, w, s)
        self.name = n
        self.fq = 100

    def purr(self, freq):
        self.fq = freq


class Bird(Animal):

    def fly(self, new_speed):
        self.run(new_speed)


my_cat = Cat('Муся', 1, 3.5, 20)
my_cat.run(5)
my_cat.purr(50)
print(my_cat.name)

bird = Bird(3, 1.5, 2)
print(bird.age)
