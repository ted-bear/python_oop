class Vehicle:

    def __init__(self, model, speed, weight):
        self._model = model
        self._speed = speed
        self._weight = weight

    def get_model(self) -> str:
        """Return vehicle's model"""
        return self._model

    def get_speed(self) -> float:
        """Return current vehicle's speed"""
        return self._speed

    def get_weight(self) -> float:
        """Return current vehicle's weight in kilogramms"""
        return self._weight


class Car(Vehicle):
    
    def __init__(self, model, speed, weight, doors_num, seat_num):
        super.__init__(model, speed, weight)
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
        super.__init__(model, speed, weight)
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




