""" Tests for the Connection module """

import unittest

from src import connection

class TestConnection(unittest.TestCase):
    """ Tests for the Connection module """

    def test_default_instantiation(self):
        """ Test a known default instantiation """
        single_connection = connection.Connection()
        self.assertFalse(single_connection.startX)
        self.assertFalse(single_connection.startY)
        self.assertFalse(single_connection.direction)
        self.assertFalse(single_connection.endX)
        self.assertFalse(single_connection.endY)

    def test_setstartX_good(self):
        """ Check that startX is set correctly with valid input """
        single_connection = connection.Connection()
        single_connection.setstartX(123)
        self.assertEqual(single_connection.startX, 123)

    def test_setstartY_good(self):
        """ Check that startY is set correctly with valid input """
        single_connection = connection.Connection()
        single_connection.setstartY(123)
        self.assertEqual(single_connection.startY, 123)

    def test_setdirection_good(self):
        """ Check that direction is set correctly with valid input """
        single_connection = connection.Connection()
        single_connection.setdirection(123)
        self.assertEqual(single_connection.direction, 123)

    def test_setendX_good(self):
        """ Check that endX is set correctly with valid input """
        single_connection = connection.Connection()
        single_connection.setendX(123)
        self.assertEqual(single_connection.endX, 123)

    def test_setendY_good(self):
        """ Check that endY is set correctly with valid input """
        single_connection = connection.Connection()
        single_connection.setendY(123)
        self.assertEqual(single_connection.endY, 123)
