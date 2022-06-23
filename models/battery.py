from datetime import datetime
from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self, service_record):
        pass

    @abstractmethod
    def __service_report(self, service_record):
        pass


class SpindlerBattery(Battery, ABC):
    def __init__(self):
        super().__init__()
        self.__battery_service_period_year = 4

    @property
    def battery_service_period_year(self):
        return self.__battery_service_period_year

    def needs_service(self, service_record):
        last_service_date = service_record.last_battery_service_date
        is_need_service = datetime.now() > last_service_date.replace(
            year=last_service_date.year + self.battery_service_period_year)
        if is_need_service:
            return self.__service_report(service_record)
        return False

    def __service_report(self, service_record):
        return f"Battery needs service." \
               f"Battery should be serviced in every {self.battery_service_period_year} years.\n" \
               f"Battery last serviced on {service_record.last_battery_service_date.strftime('%Y-%m-%d')}\n"


class NubbinBattery(Battery):
    def __init__(self):
        super().__init__()
        self.__battery_service_period_year = 4

    @property
    def battery_service_period_year(self):
        return self.__battery_service_period_year

    def needs_service(self, service_record):
        last_service_date = service_record.last_battery_service_date

        is_need_service = datetime.now() > last_service_date.replace(
            year=last_service_date.year + self.battery_service_period_year)

        if is_need_service:
            return self.__service_report(service_record.last_battery_service_date)
        return False

    def __service_report(self, service_record):
        return f"Battery needs service." \
               f"Battery should be serviced in every {self.battery_service_period_year} years.\n" \
               f"Battery last serviced on {service_record.last_battery_service_date.strftime('%Y-%m-%d')}\n"
