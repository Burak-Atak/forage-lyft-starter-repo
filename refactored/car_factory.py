from car import Car
from engine import *
from battery import *


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        return Car(
            engine=CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage, ),
            battery=SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        )

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        return Car(
            engine=WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage, ),
            battery=SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        )

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        return Car(
            engine=SternmanEngine(warning_light_on=warning_light_on),
            battery=SpindlerBattery(last_service_date=last_service_date, current_date=current_date),
        )

    @staticmethod
    def create_rorschach(
            current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        return Car(
            engine=WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage, ),
            battery=NubbinBattery(last_service_date=last_service_date, current_date=current_date),
        )

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int,
                      last_service_mileage: int):
        return Car(
            engine=CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage, ),
            battery=NubbinBattery(last_service_date=last_service_date, current_date=current_date),
        )
