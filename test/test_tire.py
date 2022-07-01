import unittest
from refactored.tire import *


class TestOctoprimeTire(unittest.TestCase):
    def test_worn_list(self):
        with self.assertRaises(AssertionError):
            OctoprimeTire([0.0, 0.0, 0.0, 0.0, 1])

        with self.assertRaises(AssertionError):
            OctoprimeTire([0.0, 0.0, 0.0, ])

        with self.assertRaises(AssertionError):
            OctoprimeTire({0.0, 0.0, 0.0, 0.0})

        with self.assertRaises(AssertionError):
            OctoprimeTire([0.0, 0.0, 0.0, "a"])

        with self.assertRaises(AssertionError):
            OctoprimeTire([-1, 0.0, 0.0, 0])

        with self.assertRaises(AssertionError):
            OctoprimeTire([0, 2, 0.0, 0])

    def test_needs_service(self):
        tire = OctoprimeTire([0.0, 0.0, 0.0, 0.0])
        self.assertFalse(tire.needs_service())
        tire.worn_list = [0.0, 1, 1, 1]
        self.assertTrue(tire.needs_service())
        tire.worn_list = [0.0, 0.9, 1, 1]
        self.assertFalse(tire.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_worn_list(self):
        with self.assertRaises(AssertionError):
            CarriganTire([0.0, 0.0, 0.0, 0.0, 1])

        with self.assertRaises(AssertionError):
            CarriganTire([0.0, 0.0, 0.0, ])

        with self.assertRaises(AssertionError):
            CarriganTire({0.0, 0.0, 0.0, 0.0})

        with self.assertRaises(AssertionError):
            CarriganTire([0.0, 0.0, 0.0, "a"])

        with self.assertRaises(AssertionError):
            CarriganTire([-1, 0.0, 0.0, 0])

        with self.assertRaises(AssertionError):
            CarriganTire([0, 2, 0.0, 0])

    def test_needs_service(self):
        tire = CarriganTire([0.0, 0.0, 0.0, 0.0])
        self.assertFalse(tire.needs_service())
        tire.worn_list = [0.0, 0.9, 0, 0]
        self.assertTrue(tire.needs_service())
        tire.worn_list = [0.0, 0.8, 0, 0]
        self.assertFalse(tire.needs_service())
