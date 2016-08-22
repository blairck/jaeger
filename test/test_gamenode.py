""" Tests for the GameNode module """

from contextlib import contextmanager
from io import StringIO
import sys
import unittest

from src import gamenode

@contextmanager
def captured_output():
    """ Redirects stdout to StringIO so we can inspect Print statements """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestGameNode(unittest.TestCase):
    """ Tests for the GameNode module """

    def test_default_instantiation(self):
        """ Test a known default instantiation """
        gn_obj = gamenode.GameNode()
        result = gn_obj.gameState[0][0]
        self.assertEqual(result, -1)
        self.assertFalse(gn_obj.leafP)
        self.assertFalse(gn_obj.rootP)
        self.assertFalse(gn_obj.score)

    def test_initialize(self):
        """ Test initialization """
        gn_obj = gamenode.GameNode()
        result = gn_obj.initialize()
        self.assertFalse(result)

    def test_getState_default(self):
        """ Test a known getState value """
        gn_obj = gamenode.GameNode()
        result = gn_obj.getState(0, 0)
        self.assertEqual(result, -1)

    def test_getState_bad_location(self):
        """ Test getState with a bad location """
        gn_obj = gamenode.GameNode()
        self.assertRaises(IndexError, gn_obj.getState, 0, 100)

    def test_setState_good_location(self):
        """ Test setState with good location """
        gn_obj = gamenode.GameNode()
        gn_obj.setState(0, 0, 5)
        result = gn_obj.getState(0, 0)
        self.assertEqual(result, 5)

    def test_setState_bad_location(self):
        """ Test setState with bad location """
        gn_obj = gamenode.GameNode()
        self.assertRaises(IndexError, gn_obj.setState, 0, 100, 5)


    def test_print_board(self):
        """Check that print_board works"""
        with captured_output() as out:
            gn_obj = gamenode.GameNode()
            gn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("-1-1-1   \n"
                              "   -1-1-1   \n"
                              "-1-1-1-1-1-1-1\n"
                              "-1-1-1-1-1-1-1\n"
                              "-1-1-1-1-1-1-1\n"
                              "   -1-1-1   \n"
                              "   -1-1-1")
            self.assertEqual(actual_print, expected_print)
