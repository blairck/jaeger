""" Tests for the main module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from src import ai
from src import historynode
from test import helper
import main

class TestMain(unittest.TestCase):
    """ Tests for the Main module """

    def test_aPlayerHasWon_false(self):
        hnObject = helper.nearlyDrawnGame
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
