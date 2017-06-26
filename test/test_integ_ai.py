""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode
from src import rules

class TestIntegAI(unittest.TestCase):
    """ Integration Tests for the AI module """

    def test_getMovesForFoxPiece_MixedConnections(self):
        """ Check case when fox has mixed move connections """
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI(0.5, 0.5)
        expectedValue_initial = types.EMPTY
        expectedValue_end = types.FOX
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        actualValue_inital = actualValue[0].getState(fox_location)
        actualValue_end = actualValue[0].getState(coordinate.Coordinate(3, 5))
        self.assertEqual(len(actualValue), 4)
        self.assertEqual(actualValue_inital, expectedValue_initial)
        self.assertEqual(actualValue_end, expectedValue_end)

    def test_getMovesForFoxPieceHelper(self):
        """ Check getMovesForFoxPiece helper function """
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        fox_destination = coordinate.Coordinate(2, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI(0.5, 0.5)
        expectedValue_initial = types.EMPTY
        expectedValue_end = types.FOX
        actualValue = ai_object.getMovesForFoxPieceHelper(hn_object,
                                                          fox_location,
                                                          fox_destination)
        actualValue_initial = actualValue.getState(fox_location)
        actualValue_end = actualValue.getState(fox_destination)
        self.assertEqual(actualValue_initial, expectedValue_initial)
        self.assertEqual(actualValue_end, expectedValue_end)
