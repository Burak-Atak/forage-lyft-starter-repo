from datetime import datetime
from models.car_model import *


class ServiceRecord:
    def __init__(self, last_battery_service_date=datetime.now(), last_engine_service_miles=0,
                 miles_driven=0, is_service_light_on=False):
        self.last_battery_service_date = last_battery_service_date
        self.miles_driven = miles_driven
        self.last_engine_service_miles = last_engine_service_miles
        self.is_service_light_on = is_service_light_on


class Car:
    def __init__(self, model: CarModel, service_record: ServiceRecord):
        self.__model = model
        self.__service_record = service_record

    @property
    def model(self):
        return self.__model

    @property
    def service_record(self):
        return self.__service_record

    def needs_service(self):
        serviceable_components = self.__model.serviceable.__dict__
        should_service = []
        for component in serviceable_components.values():
                should_service.append(component.needs_service(self.__service_record))

        return should_service
