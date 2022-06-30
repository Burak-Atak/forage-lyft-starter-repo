from abc import abstractmethod, ABC


class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    def needs_service(self):
        return self.__current_mileage > 30_000 + self.__last_service_mileage


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    @property
    def current_mileage(self):
        return self.__current_mileage

    @current_mileage.setter
    def current_mileage(self, current_mileage):
        self.__current_mileage = current_mileage

    @property
    def last_service_mileage(self):
        return self.__last_service_mileage

    @last_service_mileage.setter
    def last_service_mileage(self, last_service_mileage):
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.__current_mileage > 60_000 + self.__last_service_mileage


class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.__warning_light_on = warning_light_on

    @property
    def warning_light_on(self):
        return self.__warning_light_on

    @warning_light_on.setter
    def warning_light_on(self, warning_light_on):
        self.__warning_light_on = warning_light_on

    def needs_service(self):
        return self.__warning_light_on
