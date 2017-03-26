""" Tests for the AI module """

import unittest

from res import types
from src import ai
from src import coordinate
from src import historynode

class TestRules(unittest.TestCase):
    """ Tests for the AI module """

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
