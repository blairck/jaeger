""" Tests for the HistoryNode module """

import unittest
from unittest.mock import patch

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
            expected_print = ("0 0 0    \n"
                              "    0 0 0    \n"
                              "0 0 0 0 0 0 0\n"
                              "0 0 0 0 0 0 0\n"
                              "0 0 0 0 0 0 0\n"
                              "    0 0 0    \n"
                              "    0 0 0")
            self.assertEqual(actual_print, expected_print)

    def test_pretty_print_board(self):
        """Check that pretty_print_board works"""
        with helper.captured_output() as out:
            hn_obj = historynode.HistoryNode()
            hn_obj.pretty_print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("7         . - . - .\n"
                              "          | \\ | / |\n"
                              "6         . - . - .\n"
                              "          | / | \\ |\n"
                              "5 . - . - . - . - . - . - .\n"
                              "  | \\ | / | \\ | / | \\ | / |\n"
                              "4 . - . - . - . - . - . - .\n"
                              "  | / | \\ | / | \\ | / | \\ |\n"
                              "3 . - . - . - . - . - . - .\n"
                              "          | \\ | / |\n"
                              "2         . - . - .\n"
                              "          | / | \\ |\n"
                              "1         . - . - .\n"
                              "  A   B   C   D   E   F   G")
            self.assertEqual(actual_print, expected_print)

    def test_constructor(self):
        """ Check that HistoryNode object is initialized correctly """
        hn_obj = historynode.HistoryNode()
        hn_obj.constructor()
        self.assertEqual(hn_obj.winningState, False)
        self.assertEqual(hn_obj.rootP, True)
        self.assertEqual(hn_obj.gameState[1][1], -1)
        self.assertEqual(hn_obj.gameState[6][0], -1)

        with helper.captured_output() as out:
            hn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("1 1 1    \n"
                              "    1 1 1    \n"
                              "1 1 1 1 1 1 1\n"
                              "1 1 1 1 1 1 1\n"
                              "1 1 0 0 0 1 1\n"
                              "    0 0 0    \n"
                              "    2 0 2")
            self.assertEqual(actual_print, expected_print)

        self.assertEqual(hn_obj.gameState[3][1], 0)
        self.assertEqual(hn_obj.gameState[4][0], 2)

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

    def test_determineWinningState_true(self):
        """ Check if the game state is winning """
        hn_obj = historynode.HistoryNode()
        hn_obj.determineWinningState()
        self.assertEqual(hn_obj.winningState, True)

    @patch.object(historynode.HistoryNode, "foxesWinP")
    def test_determineWinningState_false(self, mock_foxesWinP):
        """ Check if the game state is not winning """
        mock_foxesWinP.return_value = False
        hn_obj = historynode.HistoryNode()
        hn_obj.determineWinningState()
        self.assertEqual(hn_obj.winningState, False)
