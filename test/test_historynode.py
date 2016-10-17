""" Tests for the HistoryNode module """

from contextlib import contextmanager
from io import StringIO
import sys
import unittest

from src import historynode

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

class TestHistoryNode(unittest.TestCase):
    """ Tests for the historynode module, containing the HistoryNode class """

    def test_print_board(self):
        """Check that print_board works"""
        with captured_output() as out:
            hn_obj = historynode.HistoryNode()
            hn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("Player 1: None\n"
                              "Player 2: None\n"
                              "Result: None\n"
                              "Game Type: None\n"
                              "Fox Search: None\n"
                              "Goose Search: None\n"
                              "Half Move: None\n"
                              "      -1 -1 -1      \n"
                              "      -1 -1 -1      \n"
                              "-1 -1 -1 -1 -1 -1 -1\n"
                              "-1 -1 -1 -1 -1 -1 -1\n"
                              "-1 -1 -1 -1 -1 -1 -1\n"
                              "      -1 -1 -1      \n"
                              "      -1 -1 -1")
            self.assertEqual(actual_print, expected_print)
