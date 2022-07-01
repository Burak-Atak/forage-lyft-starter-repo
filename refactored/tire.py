from abc import ABC, abstractmethod


class Tire(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

    @staticmethod
    def assert_worn_list(worn_list):
        assert isinstance(worn_list, list)
        assert len(worn_list) == 4
        for worn in worn_list:
            assert isinstance(worn, float)
            assert worn >= 0.0
            assert worn <= 1.0


class CarriganTire(Tire):
    def __init__(self, worn_list: list):
        super().assert_worn_list(worn_list)
        self.worn_list = worn_list

    def needs_service(self) -> bool:
        for worn in self.worn_list:
            if worn >= 0.9:
                return True

        return False


class OctoprimeTire(Tire):
    def __init__(self, worn_list: list):
        super().assert_worn_list(worn_list)
        self.worn_list = worn_list

    def needs_service(self) -> bool:
        if sum(self.worn_list) >= 3:
            return True

        return False
