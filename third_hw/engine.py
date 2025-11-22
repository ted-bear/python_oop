class Engine:

    def __init__(self, name, horsepowers):
        self._name = name
        self._horsepowers = horsepowers
    
    def get_name(self) -> str:
        return self._name

    def get_horsepowers(self) -> int:
        return self._horsepowers


class ICEEngine(Engine):

    def __init__(self, name, horsepowers, volume, cycle_number):
        super.__init__(name, horsepowers)
        self.__volume = volume
        self.__cycle_number = cycle_number

    def get_volume(self) -> float:
        return self.__volume

    def get_cycle_number(self) -> int:
        return self.__cycle_number


class ElectricEngine(Engine):

    def __init__(self, name, horsepowers, battery_volume):
        super.__init__(name, horsepowers)
        self.__battery_volume = battery_volume

    def start(self):
        self.__battery_volume -= 1

    def charge(self, volume):
        self.__battery_volume += volume


