""" Tests for the HistoryNode module """

import unittest

from src import historynode
from test import helper

class TestHistoryNode(unittest.TestCase):
    """ Tests for the historynode module, containing the HistoryNode class """

    # pylint: disable=too-many-public-methods
    # Never too many tests

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

    def test_geeseWinP_good(self):
        """ Check that geeseWinP can detect a clear win state """
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        hn_obj.gameState[2][0] = 1
        hn_obj.gameState[2][1] = 3
        hn_obj.gameState[2][2] = 1
        hn_obj.gameState[3][0] = 1
        hn_obj.gameState[3][1] = 1
        hn_obj.gameState[3][2] = 3
        hn_obj.gameState[4][0] = 1
        hn_obj.gameState[4][1] = 3
        hn_obj.gameState[4][2] = 1
        expected_result = True
        actual_result = hn_obj.geeseWinP()
        self.assertEqual(actual_result, expected_result)

    def test_geeseWinP_not_quite(self):
        """ Check that geeseWinP detects that an almost win isn't a win"""
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        hn_obj.gameState[2][0] = 1
        hn_obj.gameState[2][2] = 1
        hn_obj.gameState[3][0] = 1
        hn_obj.gameState[3][1] = 1
        hn_obj.gameState[3][2] = 3
        hn_obj.gameState[4][0] = 1
        hn_obj.gameState[4][1] = 3
        hn_obj.gameState[4][2] = 1
        expected_result = False
        actual_result = hn_obj.geeseWinP()
        self.assertEqual(actual_result, expected_result)

    def test_geeseWinP_not_at_all(self):
        """ Check that geeseWinP detects that starting position isn't a win"""
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        expected_result = False
        actual_result = hn_obj.geeseWinP()
        self.assertEqual(actual_result, expected_result)

    def test_foxesWinP_good(self):
        """ Check that foxesWinP can detect a clear win state """
        hn_obj = historynode.HistoryNode()
        # Don't run the constructor since it populates Geese pieces
        hn_obj.gameState[2][0] = 1
        hn_obj.gameState[2][2] = 1
        hn_obj.gameState[3][0] = 1
        hn_obj.gameState[3][1] = 1
        hn_obj.gameState[3][2] = 3
        hn_obj.gameState[4][0] = 1
        hn_obj.gameState[4][1] = 3
        hn_obj.gameState[4][2] = 1
        expected_result = True
        actual_result = hn_obj.foxesWinP()
        self.assertEqual(actual_result, expected_result)

    def test_foxesWinP_not_quite(self):
        """ Check that foxesWinP detects that an almost win isn't a win"""
        hn_obj = historynode.HistoryNode()
        # Don't run the constructor since it populates Geese pieces
        hn_obj.gameState[1][2] = 1
        hn_obj.gameState[2][2] = 3
        hn_obj.gameState[3][2] = 1
        hn_obj.gameState[4][6] = 1
        hn_obj.gameState[4][5] = 1
        hn_obj.gameState[4][4] = 3
        hn_obj.gameState[2][0] = 3
        hn_obj.gameState[3][0] = 3
        hn_obj.gameState[4][0] = 3
        hn_obj.gameState[4][1] = 3
        expected_result = False
        actual_result = hn_obj.foxesWinP()
        self.assertEqual(actual_result, expected_result)

    def test_foxesWinP_not_at_all(self):
        """ Check that foxesWinP detects that starting position isn't a win"""
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        expected_result = False
        actual_result = hn_obj.foxesWinP()
        self.assertEqual(actual_result, expected_result)

    def test_setGameType_good(self):
        """ Check that gameType is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setGameType(123)
        self.assertEqual(hn_obj.gameType, 123)

    def test_setGameType_bad(self):
        """ Check that gameType is raises an error with non-int input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setGameType, "abc")

    def test_setFoxSearch_good(self):
        """ Check that foxSearch is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setFoxSearch(123)
        self.assertEqual(hn_obj.foxSearch, 123)

    def test_setFoxSearch_bad(self):
        """ Check that foxSearch is raises an error with non-int input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setFoxSearch, "abc")

    def test_setResult_good(self):
        """ Check that result is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setResult(123)
        self.assertEqual(hn_obj.result, 123)

    def test_setResult_bad(self):
        """ Check that result is raises an error with non-int input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setResult, "abc")

    def test_setGooseSearch_good(self):
        """ Check that gooseSearch is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setGooseSearch(123)
        self.assertEqual(hn_obj.gooseSearch, 123)

    def test_setGooseSearch_bad(self):
        """ Check that gooseSearch is raises an error with non-int input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setGooseSearch, "abc")

    def test_setHalfMove_good(self):
        """ Check that halfMove is set correctly with valid input """
        hn_obj = historynode.HistoryNode()
        hn_obj.setHalfMove(123)
        self.assertEqual(hn_obj.halfMove, 123)

    def test_setHalfMove_bad(self):
        """ Check that halfMove is raises an error with non-int input """
        hn_obj = historynode.HistoryNode()
        self.assertRaises(TypeError, hn_obj.setHalfMove, "abc")
