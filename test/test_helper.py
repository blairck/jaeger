""" Tests for the helper module """

import unittest

from src import helper

class TestHelper(unittest.TestCase):
    """ Tests for the helper module """
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
