""" Tests for the main module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import historynode
from src import coordinate
import main

class TestMain(unittest.TestCase):
    """ Tests for the Main module """

    def test_aPlayerHasWon_false(self):
        r"""
        7         S - . - .
                  | \ | / |
        6         S - . - .
                  | / | \ |
        5 . - . - . - . - . - . - .
          | \ | / | \ | / | \ | / |
        4 . - . - . - . - S - . - .
          | / | \ | / | \ | / | \ |
        3 . - . - S - S - S - . - .
                  | \ | / |
        2         S - S - ~
                  | / | \ |
        1         F - F - S
          1   2   3   4   5   6   7
        """
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(3, 1), types.FOX)
        hnObject.setState(coordinate.Coordinate(4, 1), types.FOX)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 4), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 6), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 7), types.SUPERGOOSE)
        actualResult = main.aPlayerHasWon(hnObject)
        self.assertEqual(actualResult, False)

    @patch.object(historynode.HistoryNode, "geeseWinP")
    def test_aPlayerHasWon_geeseWin(self, mock_geeseWinP):
        mock_geeseWinP.return_value = True
        hnObject = historynode.HistoryNode()
        actualResult = main.aPlayerHasWon(hnObject)
        self.assertEqual(actualResult, True)

    @patch.object(historynode.HistoryNode, "foxesWinP")
    def test_aPlayerHasWon_foxesWin(self, mock_foxesWinP):
        mock_foxesWinP.return_value = True
        hnObject = historynode.HistoryNode()
        actualResult = main.aPlayerHasWon(hnObject)
        self.assertEqual(actualResult, True)

    @patch.object(ai.AI, "evaluationFunction")
    def test_determineDraw_not_draw(self, mock_evaluationFunction):
        mock_evaluationFunction.return_value = True
        aiObject = ai.AI()
        hnObject = historynode.HistoryNode()
        actualResult = main.determineDraw(hnObject, aiObject)
        self.assertEqual(actualResult, False)

    @patch.object(ai.AI, "evaluationFunction")
    def test_determineDraw_draw(self, mock_evaluationFunction):
        mock_evaluationFunction.return_value = None
        aiObject = ai.AI()
        hnObject = historynode.HistoryNode()
        actualResult = main.determineDraw(hnObject, aiObject)
        self.assertEqual(actualResult, True)

    @patch.object(historynode.HistoryNode, "setState")
    def test_setTwoRandomFoxCoordinatesInVictoryArea(self, theMock):
        hnObject = historynode.HistoryNode()
        main.setTwoRandomFoxCoordinatesInVictoryArea(hnObject)
        self.assertEqual(theMock.call_count, 2)

    @patch.object(historynode.HistoryNode, "setState")
    def test_createStartingPosition_standard_true(self, theMock):
        main.createStartingPosition(True)
        self.assertEqual(theMock.call_count, 26)

    @patch.object(main, "setTwoRandomFoxCoordinatesInVictoryArea")
    def test_createStartingPosition_standard_false(self, theMock):
        main.createStartingPosition(False)
        self.assertEqual(theMock.call_count, 1)
