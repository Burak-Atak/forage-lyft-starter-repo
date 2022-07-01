from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from tire import Tire


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.__engine = engine
        self.__battery = battery
        self.__tire = tire

    @property
    def engine(self):
        return self.__engine

    @property
    def battery(self):
        return self.__battery

    @property
    def tire(self):
        return self.__tire

    def needs_service(self):
        return any(
            [
                self.__engine.needs_service(),
                self.__battery.needs_service(),
                self.__tire.needs_service(),
            ]
        )
