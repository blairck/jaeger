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
                              "      0 0 0      \n"
                              "      0 0 0      \n"
                              "0 0 0 0 0 0 0\n"
                              "0 0 0 0 0 0 0\n"
                              "0 0 0 0 0 0 0\n"
                              "      0 0 0      \n"
                              "      0 0 0")
            self.assertEqual(actual_print, expected_print)

    def test_constructor(self):
        """ Check that HistoryNode object is initialized correctly """
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

        with helper.captured_output() as out:
            hn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("Player 1: None\n"
                              "Player 2: None\n"
                              "Result: 0\n"
                              "Game Type: 1\n"
                              "Fox Search: 1\n"
                              "Goose Search: 1\n"
                              "Half Move: 1\n"
                              "      1 1 1      \n"
                              "      1 1 1      \n"
                              "1 1 1 1 1 1 1\n"
                              "1 1 1 1 1 1 1\n"
                              "1 1 0 0 0 1 1\n"
                              "      0 0 0      \n"
                              "      2 0 2")
            self.assertEqual(actual_print, expected_print)

        self.assertEqual(hn_obj.gameState[3][1], 0)
        self.assertEqual(hn_obj.gameState[4][0], 2)

    def test_setP1_good(self):
        """ Check that P1 is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setP1("abc")
        self.assertEqual(hn_obj.p1, "abc")

    def test_setP1_bad(self):
        """ Check that P1 is raises an error with non-string input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setP1, 10)

    def test_setP2_good(self):
        """ Check that P2 is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setP2("abc")
        self.assertEqual(hn_obj.p2, "abc")

    def test_setP2_bad(self):
        """ Check that P2 is raises an error with non-string input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setP2, 10)
