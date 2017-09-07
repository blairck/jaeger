""" Tests for the AI module """

import unittest

# pylint: disable=import-error
from res import types
from src import coordinate
from src import historynode
from src import interface

class TestInterface(unittest.TestCase):
    """ Integration Tests for the Interface module """

    def test_getPositionFromListOfMoves_goose(self):
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
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(hnObject, gooseP)
        actualValue = interface.getPositionFromListOfMoves(listOfMoves,
                                                           "24",
                                                           gooseP)
        # Todo write more

    def test_getPositionFromListOfMoves_fox(self):
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
        # Todo write this test
