from models import engine
from models import battery


class Serviceable:
    def __init__(self, engine: engine.Engine, battery: battery.Battery, attributes=None):

        self.engine = engine
        self.battery = battery
        if attributes:
            assert isinstance(attributes, dict)
            for key, value in attributes.items():
                setattr(self, key, value)


class Unserviceable:
    def __init__(self, attributes=None):
        if attributes:
            assert isinstance(attributes, dict)
            for key, value in attributes.items():
                setattr(self, key, value)


class CarModel:
    def __init__(self, serviceable: Serviceable, unserviceable: Unserviceable):
        self.serviceable = serviceable
        self.unserviceable = unserviceable


# Batteries
spindler_battery = battery.SpindlerBattery()
nubbin_battery = battery.NubbinBattery()

# Engines
capulet_engine = engine.CapuletEngine()
willoughby_engine = engine.WilloughbyEngine()
sternman_engine = engine.SternmanEngine()


class Calliope(CarModel):
    def __init__(self):
        super().__init__(serviceable=Serviceable(engine=capulet_engine, battery=spindler_battery),
                         unserviceable=Unserviceable())


class Glissade(CarModel):
    def __init__(self):
        super().__init__(serviceable=Serviceable(engine=willoughby_engine, battery=spindler_battery),
                         unserviceable=Unserviceable())


class Palindrome(CarModel):
    def __init__(self):
        super().__init__(serviceable=Serviceable(engine=sternman_engine, battery=spindler_battery),
                         unserviceable=Unserviceable())


class Rorschach(CarModel):
    def __init__(self):
        super().__init__(serviceable=Serviceable(engine=capulet_engine, battery=nubbin_battery),
                         unserviceable=Unserviceable())


class Thovex(CarModel):
    def __init__(self):
        super().__init__(serviceable=Serviceable(engine=capulet_engine, battery=nubbin_battery),
                         unserviceable=Unserviceable())
