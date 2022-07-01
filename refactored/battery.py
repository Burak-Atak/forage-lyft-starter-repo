from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        assert isinstance(last_service_date, datetime)
        assert isinstance(current_date, datetime)
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    @property
    def last_service_date(self):
        return self.__last_service_date

    @property
    def current_date(self):
        return self.__current_date

    @last_service_date.setter
    def last_service_date(self, last_service_date):
        self.__last_service_date = last_service_date

    def needs_service(self):
        return self.__current_date > self.__last_service_date.replace(
            year=self.__last_service_date.year + 3)


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        assert isinstance(last_service_date, datetime)
        assert isinstance(current_date, datetime)
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    @property
    def last_service_date(self):
        return self.__last_service_date

    @last_service_date.setter
    def last_service_date(self, last_service_date):
        self.__last_service_date = last_service_date

    @property
    def current_date(self):
        return self.__current_date

    @last_service_date.setter
    def last_service_date(self, last_service_date):
        self.__last_service_date = last_service_date

    def needs_service(self):
        return self.__current_date > self.__last_service_date.replace(
            year=self.__last_service_date.year + 4)
