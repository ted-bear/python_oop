class Cat:
    name = 'Барсик'
    age = 0
    weight = 0.1
    speed = 0
    fq = 100

    def __init__(self, cat_name, cat_age, cat_weight, cat_speed, cat_fq):
        self.name = cat_name
        self.age = cat_age
        self.weight = cat_weight
        self.speed = cat_speed
        self.fq = cat_fq

    def Run(self, new_speed):
        self.speed = new_speed
    
    def Stop(self):
        self.speed = 0

    def Eat(self, food):
        self.weight += food

    def Purr(self, freq):
        self.fq = freq

    def Sleep(self):
        self.Stop()
        self.fq = 0
        self.weight -= 0.1

my_cat = Cat('Муся', 1, 2, 4, 100)
my_cat.Run(10)
print(my_cat.name)
