from abc import abstractmethod, ABC


class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        assert isinstance(last_service_mileage, int)
        assert isinstance(current_mileage, int)
        assert last_service_mileage >= 0
        assert current_mileage >= 0
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    @property
    def last_service_mileage(self):
        return self.__last_service_mileage

    @property
    def current_mileage(self):
        return self.__current_mileage

    @current_mileage.setter
    def current_mileage(self, value):
        self.__current_mileage = value

    @last_service_mileage.setter
    def last_service_mileage(self, value):
        self.__last_service_mileage = value

    def needs_service(self):
        return self.__current_mileage > 30_000 + self.__last_service_mileage


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        assert isinstance(last_service_mileage, int)
        assert isinstance(current_mileage, int)
        assert last_service_mileage >= 0
        assert current_mileage >= 0
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
    def __init__(self, warning_light_on: bool):
        assert isinstance(warning_light_on, bool)
        self.__warning_light_on = warning_light_on

    @property
    def warning_light_on(self):
        return self.__warning_light_on

    @warning_light_on.setter
    def warning_light_on(self, warning_light_on):
        self.__warning_light_on = warning_light_on

    def needs_service(self):
        return self.__warning_light_on
