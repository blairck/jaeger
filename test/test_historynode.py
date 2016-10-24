""" Tests for the HistoryNode module """

import unittest

from src import historynode
from test import helper

class TestHistoryNode(unittest.TestCase):
    """ Tests for the historynode module, containing the HistoryNode class """

    def test_print_board(self):
        """Check that print_board works"""
        with helper.captured_output() as out:
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

    def test_constructor(self):
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        self.assertEqual(hn_obj.leafP, False)
        self.assertEqual(hn_obj.rootP, True)
        self.assertEqual(hn_obj.result, 0)
        self.assertEqual(hn_obj.gameType, 1)
        self.assertEqual(hn_obj.foxSearch, 1)
        self.assertEqual(hn_obj.gooseSearch, 1)
        self.assertEqual(hn_obj.halfMove, 1)
        self.assertEqual(hn_obj.gameState[1][1], -1)
        self.assertEqual(hn_obj.gameState[6][0], -1)