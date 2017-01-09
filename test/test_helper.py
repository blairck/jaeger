import unittest

from src import coordinate
from src import helper

class TestHistoryNode(unittest.TestCase):
    def test_checkIfInt_good(self):
        """ Check that checkIfInt correctly assesses an input """
        self.assertFalse(helper.checkIfInt(123))

    def test_checkIfInt_bad(self):
        """ Check that checkIfInt raises an error with non-int input """
        self.assertRaises(TypeError, helper.checkIfInt, "abc")

    def test_checkIfCoordinateIsValid_good(self):
        """ Check that checkIfCoordinateIsValid doesn't raise exception """
        self.assertFalse(helper.checkIfCoordinateIsValid(3, 4))

    def test_checkIfCoordinateIsValid_bad_x(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertRaises(ValueError,
                          helper.checkIfCoordinateIsValid,
                          30, 4)

    def test_checkIfCoordinateIsValid_bad_y(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertRaises(ValueError,
                          helper.checkIfCoordinateIsValid,
                          3, 40)

    def test_checkIfCoordinateIsValid_bad_x_y(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertRaises(ValueError,
                          helper.checkIfCoordinateIsValid,
                          50, 40)

    def test_checkIfCoordinateIsValid_bad_location_x_y(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertRaises(ValueError,
                          helper.checkIfCoordinateIsValid,
                          1, 1)

    def test_checkIfCoordinateIsValid_good_location_x(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertFalse(helper.checkIfCoordinateIsValid(1, 3))

    def test_checkIfCoordinateIsValid_good_location_y(self):
        """ Check that checkIfCoordinateIsValid does raise an exception """
        self.assertFalse(helper.checkIfCoordinateIsValid(6, 4))
