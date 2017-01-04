import unittest

from src import helper

class TestHistoryNode(unittest.TestCase):
    def test_checkIfInt_good(self):
        """ Check that checkIfInt correctly assesses an input """
        self.assertFalse(helper.checkIfInt(123))

    def test_checkIfInt_bad(self):
        """ Check that checkIfInt raises an error with non-int input """
        self.assertRaises(TypeError, helper.checkIfInt, "abc")