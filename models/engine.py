from abc import abstractmethod, ABC


class Engine(ABC):

    @abstractmethod
    def needs_service(self, service_record):
        pass

    @abstractmethod
    def __service_report(self, service_record):
        pass


class CapuletEngine(Engine, ABC):
    def __init__(self):
        super().__init__()
        self.miles_for_service = 30_000

    def needs_service(self, service_record):
        is_need_service = service_record.miles_driven > self.miles_for_service + service_record.last_engine_service_miles
        if is_need_service:
            return self.__service_report(service_record)
        return False

    def __service_report(self, service_record):
        return f"Engine needs service.\n" \
               f"Engine should be serviced in every {self.miles_for_service} miles.\n" \
               f"Engine last serviced on {service_record.last_engine_service_miles} miles.\n"


class WilloughbyEngine(Engine, ABC):
    def __init__(self):
        super().__init__()
        self.miles_for_service = 60_000

    def needs_service(self, service_record):
        is_need_service = service_record.miles_driven > self.miles_for_service + service_record.last_engine_service_miles
        if is_need_service:
            return self.__service_report(service_record)

    def __service_report(self, service_record):
        return f"Engine needs service.\n" \
               f"Engine should be serviced in every {self.miles_for_service} miles.\n" \
               f"Engine last serviced on {service_record.last_engine_service_miles} miles.\n"


class SternmanEngine(Engine, ABC):
    def __init__(self):
        super().__init__()
        self.is_service_light_on = False

    def needs_service(self, service_record):
        is_need_service = service_record.is_service_light_on
        if is_need_service:
            return self.__service_report(service_record)
        return False

    def __service_report(self, service_record):
        return f"Engine need service." \
               f"Engine service light is on.\n"
