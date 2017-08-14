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

    def test_getMovesForGoosePiece_GooseToSuper(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        goose_xBoard = 2
        goose_yBoard = 3
        gooseLocation = coordinate.Coordinate(goose_xBoard, goose_yBoard)
        gooseDestination0 = coordinate.Coordinate(goose_xBoard + 1,
                                                  goose_yBoard)
        gooseDestination1 = coordinate.Coordinate(goose_xBoard - 1,
                                                  goose_yBoard)
        hnObject.setState(gooseLocation, types.GOOSE)
        resultingMoves = aiObject.getMovesForGoosePiece(hnObject,
                                                        gooseLocation)
        numberOfMoves = len(resultingMoves)
        self.assertEqual(numberOfMoves, 2)
        self.assertEqual(resultingMoves[0].getState(gooseLocation),
                         types.EMPTY)
        self.assertEqual(resultingMoves[0].getState(gooseDestination0),
                         types.SUPERGOOSE)
        self.assertEqual(resultingMoves[1].getState(gooseLocation),
                         types.EMPTY)
        self.assertEqual(resultingMoves[1].getState(gooseDestination1),
                         types.GOOSE)

    def test_getMovesForGoosePiece_MaxMoves(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(gooseLocation, types.GOOSE)
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 5)

    def test_getMovesForGoosePiece_PartialMoves(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(4, 7)
        hnObject.setState(gooseLocation, types.GOOSE)
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 3)

    def test_getMovesForGoosePiece_SuperGoose(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(5, 3)
        hnObject.setState(gooseLocation, types.SUPERGOOSE)
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 7)

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
