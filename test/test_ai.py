""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode
from src import rules

class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForFoxPiece(self, mock_legalMoveP):
        """ Check case when fox move exists and is legal """
        mock_legalMoveP.return_value = True
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI(0.5, 0.5)
        expectedValue_initial = types.EMPTY
        expectedValue_end = types.FOX
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        actualValue_inital = actualValue[0].getState(fox_location)
        actualValue_end = actualValue[0].getState(coordinate.Coordinate(3, 5))
        self.assertEqual(len(actualValue), 8)
        self.assertEqual(actualValue_inital, expectedValue_initial)
        self.assertEqual(actualValue_end, expectedValue_end)

    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForFoxPiece_none_legal(self, mock_legalMoveP):
        """ Check case when fox move exists and is legal """
        mock_legalMoveP.return_value = False
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI(0.5, 0.5)
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        self.assertEqual(len(actualValue), 0) # No legal moves

    def test_getAllFoxCaptures_dir_5(self):
        """ Correctly evaluate a simple game position """
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        goose_location = coordinate.Coordinate(3, 3)
        hn_object.setState(fox_location, types.FOX)
        hn_object.setState(goose_location, types.GOOSE)
        ai_object = ai.AI(0.5, 0.5)
        actualValue = ai_object.getAllFoxCaptures(hn_object, fox_location)
        actualValue_inital = actualValue[0].getState(fox_location)
        actualValue_middle = actualValue[0].getState(goose_location)
        actualValue_end = actualValue[0].getState(coordinate.Coordinate(3, 2))
        actualValue_length = len(actualValue)
        expectedValue_initial = types.EMPTY
        expectedValue_middle = types.EMPTY
        expectedValue_end = types.FOX
        expectedValue_length = 1
        self.assertEqual(actualValue_inital, expectedValue_initial)
        self.assertEqual(actualValue_middle, expectedValue_middle)
        self.assertEqual(actualValue_end, expectedValue_end)
        self.assertEqual(actualValue_length, expectedValue_length)

    def test_getAllFoxCaptures_complicated(self):
        """ Correctly evaluate a complicated game position """
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(5, 6)
        goose_location1 = coordinate.Coordinate(5, 5)
        goose_location2 = coordinate.Coordinate(6, 4)
        goose_location3 = coordinate.Coordinate(4, 4)
        goose_location4 = coordinate.Coordinate(4, 3)
        hn_object.setState(fox_location, types.FOX)
        hn_object.setState(goose_location1, types.GOOSE)
        hn_object.setState(goose_location2, types.GOOSE)
        hn_object.setState(goose_location3, types.GOOSE)
        hn_object.setState(goose_location4, types.GOOSE)
        ai_object = ai.AI(0.5, 0.5)
        actualValue = ai_object.getAllFoxCaptures(hn_object, fox_location)
        actualValue_length = len(actualValue)

        actualValue_inital = actualValue[0].getState(fox_location)
        actualValue_middle = actualValue[0].getState(goose_location1)
        endLocation = coordinate.Coordinate(5, 4)
        actualValue_end = actualValue[0].getState(endLocation)
        self.assertEqual(actualValue_inital, types.EMPTY)
        self.assertEqual(actualValue_middle, types.EMPTY)
        self.assertEqual(actualValue_end, types.FOX)

        actualValue_inital = actualValue[1].getState(fox_location)
        actualValue_middle = actualValue[1].getState(goose_location2)
        endLocation = coordinate.Coordinate(7, 4)
        actualValue_end = actualValue[1].getState(endLocation)
        self.assertEqual(actualValue_inital, types.EMPTY)
        self.assertEqual(actualValue_middle, types.EMPTY)
        self.assertEqual(actualValue_end, types.FOX)

        actualValue_inital = actualValue[2].getState(fox_location)
        actualValue_middle = actualValue[2].getState(goose_location3)
        endLocation = coordinate.Coordinate(3, 4)
        actualValue_end = actualValue[2].getState(endLocation)
        actualValue_outside_goose = actualValue[2].getState(goose_location4)
        self.assertEqual(actualValue_inital, types.EMPTY)
        self.assertEqual(actualValue_middle, types.EMPTY)
        self.assertEqual(actualValue_end, types.FOX)

        self.assertEqual(actualValue_length, 3)
        self.assertEqual(actualValue_outside_goose, types.GOOSE)

    def test_evaluationFunction_default(self):
        """ Correctly evaluate a default game position """
        hn_object = historynode.HistoryNode()
        ai_object = ai.AI(0.5, 0.5)
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1010.0
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_single_goose(self):
        """ Correctly evaluate a game with a single goose """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 6), types.GOOSE)
        ai_object = ai.AI(1, 1)
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1019.0
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_single_supergoose(self):
        """ Correctly evaluate a supergoose """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 6), types.SUPERGOOSE)
        ai_object = ai.AI(1, 1)
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1018.0
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_supergoose_in_fox_area(self):
        """ Correctly evaluate a supergoose in the fox starting area """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        ai_object = ai.AI(1, 1)
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1015.0
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_winning_goose(self):
        """ Correctly evaluate a winning goose position """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hn_object.setState(coordinate.Coordinate(4, 1), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(5, 1), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(3, 2), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(4, 2), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(5, 2), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(3, 3), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(4, 3), types.GOOSE)
        hn_object.setState(coordinate.Coordinate(5, 3), types.GOOSE)
        ai_object = ai.AI(1, 1)
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = 993.0
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_transferNode(self):
        """ Correctly transfer a historynode """
        hn_object = historynode.HistoryNode()
        location = coordinate.Coordinate(3, 3)
        hn_object.setState(location, types.SUPERGOOSE)
        result = ai.transferNode(hn_object)
        actualValue = result.getState(location)
        expectedValue = types.SUPERGOOSE
        self.assertEqual(actualValue, expectedValue)
