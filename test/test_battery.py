import unittest
from datetime import datetime, timedelta
from refactored.battery import *


class TestSpindlerBattery(unittest.TestCase):
    def test_types(self):
        with self.assertRaises(AssertionError):
            battery = SpindlerBattery(last_service_date="adf", current_date="sdf")

        with self.assertRaises(AssertionError):
            battery = SpindlerBattery(last_service_date=2, current_date=datetime.now())

        with self.assertRaises(AssertionError):
            battery = SpindlerBattery(last_service_date=datetime.now(), current_date="sdf")

    def test_needs_service(self):
        battery = SpindlerBattery(last_service_date=datetime.now(), current_date=datetime.now())
        self.assertFalse(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=1500)
        self.assertTrue(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=3669)
        self.assertTrue(battery.needs_service())
        battery.last_service_date = datetime.now() + timedelta(days=367)
        self.assertFalse(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=1097)
        self.assertTrue(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_types(self):
        with self.assertRaises(AssertionError):
            battery = NubbinBattery(last_service_date="adf", current_date="sdf")

        with self.assertRaises(AssertionError):
            battery = NubbinBattery(last_service_date=2, current_date=datetime.now())

        with self.assertRaises(AssertionError):
            battery = NubbinBattery(last_service_date=datetime.now(), current_date="sdf")

    def test_needs_service(self):
        battery = NubbinBattery(last_service_date=datetime.now(), current_date=datetime.now())
        self.assertFalse(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=1500)
        self.assertTrue(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=3669)
        self.assertTrue(battery.needs_service())
        battery.last_service_date = datetime.now() + timedelta(days=367)
        self.assertFalse(battery.needs_service())
        battery.last_service_date = datetime.now() - timedelta(days=1400)
        self.assertFalse(battery.needs_service())
