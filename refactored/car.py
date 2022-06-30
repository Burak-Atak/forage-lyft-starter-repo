from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    @property
    def engine(self):
        return self.__engine

    @property
    def battery(self):
        return self.__battery

    def needs_service(self):
        return all(
            [
                self.__engine.needs_service(),
                self.__battery.needs_service(),
            ]
        )
