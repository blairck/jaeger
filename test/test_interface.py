""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode
from src import interface
from test import helper

class TestInterface(unittest.TestCase):
    """ Integration Tests for the Interface module """

    @classmethod
    def setUpClass(cls):
        cls.shared_game = helper.nearlyWonGooseGame

    @patch.object(interface, "matchSingleCoordinateToMoves")
    def test_getPositionFromListOfMoves_single(self,
                                               mock_matchSingleCoordinateTo):
        """ Get position from list of moves with a single coordinate string
        input """
        mock_matchSingleCoordinateTo.return_value = ["fake board1"]
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(listOfMoves,
                                                      '53',
                                                      gooseP)
        self.assertEqual(len(result), 1)

    @patch.object(interface, "matchMultipleCoordinatesToMoves")
    def test_getPositionFromListOfMoves_multi(self,
                                              mock_matchMultipleCoordinatesTo):
        """ Get position from list of moves with a multi coordinate string
        input """
        mock_matchMultipleCoordinatesTo.return_value = ["fake_board1",
                                                        "fake_board2"]
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(listOfMoves,
                                                      '5363',
                                                      gooseP)
        self.assertEqual(len(result), 2)

    def test_getPositionFromListOfMoves_none(self):
        """ Gets a simple position from a list of moves where none exist """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(listOfMoves,
                                                      'z1',
                                                      gooseP)
        self.assertEqual(len(result), 0)

    def test_matchSingleCoordinateToMoves_fox_unambiguous(self):
        """ Match coordinate where there is exactly one match """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 5)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 1)

    def test_matchSingleCoordinateToMoves_fox_ambiguous(self):
        """ Match coordinate to moves when there are 2 matches """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 4)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 2)

    def test_matchSingleCoordinateToMoves_fox_none(self):
        """ Match coordinate to moves where there is no match """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 3)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 0)

    def test_matchMultipleCoordinatesToMoves_goose_unambiguous(self):
        """ Match multi-coordinate goose input to move """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("25-35")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_goose_more_unambiguous(self):
        """ Match multi-coordinate goose input to move """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("4233")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_goose_nonexistant(self):
        """ Get coordinates from moves where there are none """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("54-55")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_good(self):
        """ Get coordinates from good input """
        actualValue = interface.getCoordinatesFromUserInput('34')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEqual(actualValue.get_x_board(),
                         expectedValue.get_x_board())
        self.assertEqual(actualValue.get_y_board(),
                         expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_good_with_comma(self):
        """ Get coordinates from good input with comma """
        actualValue = interface.getCoordinatesFromUserInput('3,4')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEqual(actualValue.get_x_board(),
                         expectedValue.get_x_board())
        self.assertEqual(actualValue.get_y_board(),
                         expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_long(self):
        """ Get coordinates from a long input """
        actualValue = interface.getCoordinatesFromUserInput('3,4-5,6')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEqual(actualValue[0].get_x_board(),
                         expectedValue0.get_x_board())
        self.assertEqual(actualValue[1].get_y_board(),
                         expectedValue1.get_y_board())

    def test_getCoordinatesFromUserInput_long_simple(self):
        """ Get coordinates from a long input without extra notation """
        actualValue = interface.getCoordinatesFromUserInput('3456')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEqual(actualValue[0].get_x_board(),
                         expectedValue0.get_x_board())
        self.assertEqual(actualValue[1].get_y_board(),
                         expectedValue1.get_y_board())

    def test_getCoordinatesFromUserInput_bad_short(self):
        """ Parse a short bad input string """
        actualValue = interface.getCoordinatesFromUserInput('3')
        self.assertEqual(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_bad_long(self):
        """ Parse a long bad input string """
        actualValue = interface.getCoordinatesFromUserInput('345t')
        self.assertEqual(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_outside_long(self):
        """ Parse an input string outside the board """
        actualValue = interface.getCoordinatesFromUserInput('3459')
        self.assertEqual(len(actualValue), 0)

    def test_isCoordinateMatch_goose(self):
        """ Test coordinate match with goose """
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = True
        hnObject.setState(testCoordinate, types.SUPERGOOSE)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_fox(self):
        """ Test coordinate match with fox """
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        hnObject.setState(testCoordinate, types.FOX)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_empty(self):
        """ Test coordinate match when it's empty """
        hnObject = historynode.HistoryNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        self.assertFalse(interface.isCoordinateMatch(hnObject,
                                                     testCoordinate,
                                                     gooseP))

    def test_parseAlphabetNotation_simple(self):
        """ Parse a simple valid alphabetnotation input """
        actualValue = interface.parseAlphabetNotation("a3b3")
        self.assertEqual(actualValue, "1323")

    def test_parseAlphabetNotation_mixed(self):
        """ Parse a simple valid alphabetnotation input """
        actualValue = interface.parseAlphabetNotation("a323")
        self.assertEqual(actualValue, "1323")
