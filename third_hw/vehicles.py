class Vehicle:

    def __init__(self, model, speed, weight, engine):
        self._model = model
        self._speed = speed
        self._weight = weight
        self._engine = engine

    def set_engine(self, engine):
        self._engine = engine

    def get_model(self) -> str:
        """Return vehicle's model"""
        return self._model

    def get_speed(self) -> float:
        """Return current vehicle's speed"""
        return self._speed

    def get_weight(self) -> float:
        """Return current vehicle's weight in kilogramms"""
        return self._weight

    def start(self):
        self._engine.start()


class Car(Vehicle):

    def __init__(self, model, speed, weight, doors_num, seat_num, engine):
        super().__init__(model, speed, weight, engine)
        self.__doors_num = doors_num
        self.__seat_num = seat_num

    def get_doors_number(self) -> int:
        return self.__doors_num

    def get_seat_number(self) -> int:
        return self.__seat_num

    def speed_up(self, speed) -> None:
        self._speed = speed


class Truck(Vehicle):

    def __init__(self, model, speed, weight, max_cargo_weight, max_height):
        super().__init__(model, speed, weight)
        self.__cur_cargo_weight = 0
        self.__max_cargo_weight = max_cargo_weight
        self.__max_height = max_height

    def load_cargo(self, weight, height):
        new_weight = weight + self.__cur_cargo_weight
        if new_weight > self.__max_cargo_weight:
            print("The cargo is too heavy")
            return

        if height > self.__max_height:
            print("The cargo does not fit into the truck")
            return

        self.__cur_cargo_weight = new_weight
        print("The cargo is loaded")

    def unload_truck(self):
        self.__cur_cargo_weight = 0
        print("The truck is empty")

    def get_max_cargo_weight(self) -> int:
        return self.__max_cargo_weight

    def get_max_height(self) -> float:
        return self.__max_height


class Engine:

    def __init__(self, name, horsepowers):
        self._name = name
        self._horsepowers = horsepowers

    def start(self):
        pass
    
    def get_name(self) -> str:
        return self._name

    def get_horsepowers(self) -> int:
        return self._horsepowers


class ICEEngine(Engine):

    def __init__(self, name, horsepowers, volume, cycle_number):
        super().__init__(name, horsepowers)
        self.__volume = volume
        self.__cycle_number = cycle_number

    def start(self):
        print('Starting ICE engine')

    def get_volume(self) -> float:
        return self.__volume

    def get_cycle_number(self) -> int:
        return self.__cycle_number


class ElectricEngine(Engine):

    def __init__(self, name, horsepowers, battery_volume):
        super().__init__(name, horsepowers)
        self.__battery_volume = battery_volume

    def start(self):
        print('Starting electric engine')
        self.__battery_volume -= 1

    def charge(self, volume):
        self.__battery_volume += volume

if __name__ == '__main__':
    engine = ElectricEngine("electric engine", 400, 100)
    car = Car('Model X', 40, 1000, 5, 5, engine)
    car.start()

    ice_engine = ICEEngine('ICE engine', 500, 300, 5)
    car.set_engine(ice_engine)
    car.start()