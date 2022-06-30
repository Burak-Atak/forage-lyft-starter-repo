import unittest
from refactored.engine import *


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=0)
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 30_000
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 60_000
        self.assertTrue(engine.needs_service())
        engine.current_mileage = 29_999
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 30_001
        self.assertTrue(engine.needs_service())

    def test_types(self):
        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage="adf", current_mileage=0)

        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage="adf", current_mileage="sdf")

        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage=0, current_mileage="sdf")

    def test_num_greater_than_zero(self):
        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage=-1, current_mileage=0)

        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage=0, current_mileage=-1)

        with self.assertRaises(AssertionError):
            engine = CapuletEngine(last_service_mileage=-1, current_mileage=-1)


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=0)
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 30_000
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 60_000
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 59_999
        self.assertFalse(engine.needs_service())
        engine.current_mileage = 60_001
        self.assertTrue(engine.needs_service())
        engine.current_mileage = 160_001
        self.assertTrue(engine.needs_service())

    def test_types(self):
        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage="adf", current_mileage=0)

        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage="adf", current_mileage="sdf")

        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage=0, current_mileage="sdf")

        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage=2.3, current_mileage=3)


    def test_num_greater_than_zero(self):
        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage=-1, current_mileage=0)

        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage=0, current_mileage=-1)

        with self.assertRaises(AssertionError):
            engine = WilloughbyEngine(last_service_mileage=-1, current_mileage=-1)


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())
        engine.warning_light_on = True
        self.assertTrue(engine.needs_service())

    def test_types(self):
        with self.assertRaises(AssertionError):
            engine = SternmanEngine(warning_light_on="asd")

        with self.assertRaises(AssertionError):
            engine = SternmanEngine(warning_light_on=2)

        with self.assertRaises(AssertionError):
            engine = SternmanEngine(warning_light_on=4.5)


if __name__ == '__main__':
    unittest.main()
