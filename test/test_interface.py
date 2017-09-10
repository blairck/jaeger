""" Tests for the AI module """

import unittest

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode
from src import interface

class TestInterface(unittest.TestCase):
    """ Integration Tests for the Interface module """

    @classmethod
    def setUpClass(cls):
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
        """
        cls.shared_game = historynode.HistoryNode()
        cls.shared_game.setState(coordinate.Coordinate(7, 4), types.FOX)
        cls.shared_game.setState(coordinate.Coordinate(7, 5), types.FOX)
        cls.shared_game.setState(coordinate.Coordinate(2, 5), types.GOOSE)
        cls.shared_game.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
        cls.shared_game.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)

    def test_matchSingleCoordinateToMoves_fox_unambiguous(self):
        aiObject = ai.AI(0.5, 0.5)
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 5)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEquals(len(actualValue), 1)

    def test_matchSingleCoordinateToMoves_fox_ambiguous(self):
        aiObject = ai.AI(0.5, 0.5)
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 4)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEquals(len(actualValue), 2)

    def test_matchSingleCoordinateToMoves_fox_none(self):
        aiObject = ai.AI(0.5, 0.5)
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 3)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEquals(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_good(self):
        actualValue = interface.getCoordinatesFromUserInput('34')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEquals(actualValue.get_x_board(),
                          expectedValue.get_x_board())
        self.assertEquals(actualValue.get_y_board(),
                          expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_good_with_comma(self):
        actualValue = interface.getCoordinatesFromUserInput('3,4')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEquals(actualValue.get_x_board(),
                          expectedValue.get_x_board())
        self.assertEquals(actualValue.get_y_board(),
                          expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_long(self):
        actualValue = interface.getCoordinatesFromUserInput('3,4-5,6')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEquals(actualValue[0].get_x_board(),
                          expectedValue0.get_x_board())
        self.assertEquals(actualValue[1].get_y_board(),
                          expectedValue1.get_y_board())

    def test_getCoordinatesFromUserInput_long_simple(self):
        actualValue = interface.getCoordinatesFromUserInput('3456')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEquals(actualValue[0].get_x_board(),
                          expectedValue0.get_x_board())
        self.assertEquals(actualValue[1].get_y_board(),
                          expectedValue1.get_y_board())

    def test_getCoordinatesFromUserInput_bad_short(self):
        actualValue = interface.getCoordinatesFromUserInput('3')
        self.assertEquals(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_bad_long(self):
        actualValue = interface.getCoordinatesFromUserInput('345t')
        self.assertEquals(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_outside_long(self):
        actualValue = interface.getCoordinatesFromUserInput('3459')
        self.assertEquals(len(actualValue), 0)

    def test_isCoordinateMatch_goose(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = True
        hnObject.setState(testCoordinate, types.SUPERGOOSE)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_fox(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        hnObject.setState(testCoordinate, types.FOX)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_empty(self):
        aiObject = ai.AI(0.5, 0.5)
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        self.assertFalse(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))
