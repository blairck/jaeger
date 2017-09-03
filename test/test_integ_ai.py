""" Tests for the AI module """

import unittest

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode

class TestIntegAI(unittest.TestCase):
    """ Integration Tests for the AI module """

    def test_findBestMove_gooseToPlay2_3Ply(self):
        """
        7         . - . - .    
                  | \ | / |
        6         . - . - .    
                  | / | \ |
        5 . - F - . - . - . - . - .
          | \ | / | \ | / | \ | / |
        4 . - F - . - . - S - . - .
          | / | \ | / | \ | / | \ |
        3 . - . - S - S - S - . - .
                  | \ | / |
        2         S - S - ~    
                  | / | \ |
        1         S - S - S   
          1   2   3   4   5   6   7
        Goose to play. Best move is S53-52
        """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(2, 4), types.FOX)
        hnObject.setState(coordinate.Coordinate(2, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 4), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        actualValue = aiObject.findBestMove(hnObject, True, 3)
        self.assertEqual(actualValue.score, 1080.0)
        self.assertEqual(aiObject.moveCount, 1546)

    def test_findBestMove_gooseToPlay_3Ply(self):
        """
        7         . - . - .    
                  | \ | / |
        6         . - . - .    
                  | / | \ |
        5 . - G - . - . - . - . - F
          | \ | / | \ | / | \ | / |
        4 . - . - . - . - . - . - F
          | / | \ | / | \ | / | \ |
        3 . - . - ~ - S - S - . - .
                  | \ | / |
        2         S - S - S    
                  | / | \ |
        1         S - S - S   
          1   2   3   4   5   6   7
        Goose to play. Best move is G25-G24...G24-S33#
        """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(7, 4), types.FOX)
        hnObject.setState(coordinate.Coordinate(7, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(2, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        actualValue = aiObject.findBestMove(hnObject, True, 3)
        self.assertEqual(actualValue.score, 1080.0)
        self.assertEqual(aiObject.moveCount, 619)

    def test_findBestMove_foxToPlay_3Ply(self):
        """
        7         F - . - .    
                  | \ | / |
        6         . - . - .    
                  | / | \ |
        5 . - . - . - . - F - . - .
          | \ | / | \ | / | \ | / |
        4 . - . - . - G - . - G - G
          | / | \ | / | \ | / | \ |
        3 . - . - ~ - S - S - . - .
                  | \ | / |
        2         S - S - S    
                  | / | \ |
        1         S - S - S   
          1   2   3   4   5   6   7
        Fox to play. Best move is F55xG44
        """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(3, 7), types.FOX)
        hnObject.setState(coordinate.Coordinate(5, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(4, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(6, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(7, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        actualValue = aiObject.findBestMove(hnObject, False, 3)
        self.assertEqual(actualValue.score, 67.0)
        self.assertEqual(aiObject.moveCount, 511)

    def test_findBestMove_gooseToPlay_1Ply(self):
        """
        7         . - . - .    
                  | \ | / |
        6         . - . - .    
                  | / | \ |
        5 . - . - F - . - . - . - F
          | \ | / | \ | / | \ | / |
        4 . - . - . - G - . - . - .
          | / | \ | / | \ | / | \ |
        3 . - . - ~ - S - S - . - .
                  | \ | / |
        2         S - S - S    
                  | / | \ |
        1         S - S - S   
          1   2   3   4   5   6   7
        Goose to play. Best move is G44-S33#
        """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(3, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(7, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(4, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        actualValue = aiObject.findBestMove(hnObject, True, 1)
        self.assertEqual(actualValue.score, 1080.0)

    def test_findBestMove_foxToPlay_1Ply(self):
        """
        7         . - . - .    
                  | \ | / |
        6         . - . - G    
                  | / | \ |
        5 . - G - F - G - . - . - F
          | \ | / | \ | / | \ | / |
        4 . - . - . - . - . - . - .
          | / | \ | / | \ | / | \ |
        3 . - . - ~ - S - S - . - .
                  | \ | / |
        2         S - S - S    
                  | / | \ |
        1         S - S - S   
          1   2   3   4   5   6   7
        Fox to play. Best move is F35xG45xG56
        """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        hnObject.setState(coordinate.Coordinate(3, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(7, 5), types.FOX)
        hnObject.setState(coordinate.Coordinate(2, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(4, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(5, 6), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        actualValue = aiObject.findBestMove(hnObject, False, 1)
        self.assertEqual(actualValue.score, 66.5)

    def test_getMovesForGoosePiece_GooseToSuper(self):
        """ Test finding goose moves where a regular goose would be promoted
        to supergoose """
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
        """ Test regular goose with all possible moves """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(gooseLocation, types.GOOSE)
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 5)

    def test_getMovesForGoosePiece_PartialMoves(self):
        """ Test getting goose moves when only a few are available """
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(4, 7)
        hnObject.setState(gooseLocation, types.GOOSE)
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 3)

    def test_getMovesForGoosePiece_SuperGoose(self):
        """ Test supergoose has full range of motion"""
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
