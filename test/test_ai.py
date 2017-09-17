""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode
from src import rules

# pylint: disable=too-many-public-methods
class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    def test_getHighestOrLowestScoreMove_goose(self):
        """ Sort the best move of a Goose player """
        hnObjectBigScore = historynode.HistoryNode()
        hnObjectMediumScore = historynode.HistoryNode()
        hnObjectSmallScore = historynode.HistoryNode()
        hnObjectBigScore.score = 10.0
        hnObjectMediumScore.score = 1.0
        hnObjectSmallScore.score = -5.0
        allMoves = [hnObjectMediumScore, hnObjectBigScore, hnObjectSmallScore]
        gooseTurn = True
        actualMove = ai.getHighestOrLowestScoreMove(allMoves, gooseTurn)
        self.assertEqual(actualMove.score, hnObjectBigScore.score)

    def test_getHighestOrLowestScoreMove_fox(self):
        """ Get the best move of a Fox player """
        hnObjectBigScore = historynode.HistoryNode()
        hnObjectMediumScore = historynode.HistoryNode()
        hnObjectSmallScore = historynode.HistoryNode()
        hnObjectBigScore.score = 10.0
        hnObjectMediumScore.score = 1.0
        hnObjectSmallScore.score = -5.0
        allMoves = [hnObjectMediumScore, hnObjectBigScore, hnObjectSmallScore]
        gooseTurn = False
        actualMove = ai.getHighestOrLowestScoreMove(allMoves, gooseTurn)
        self.assertEqual(actualMove.score, hnObjectSmallScore.score)

    @patch.object(ai.AI, "getMovesForGoosePiece")
    def test_getAllMovesForPlayer_goose(self, mock_getMovesForGoosePiece):
        """ Get moves for a Goose player """
        mock_getMovesForGoosePiece.return_value = ["fake board"]
        aiObject = ai.AI()
        hnObject = historynode.HistoryNode()
        gooseP = True
        actualValue = len(aiObject.getAllMovesForPlayer(hnObject, gooseP))
        expectedValue = 33
        self.assertEqual(actualValue, expectedValue)

    @patch.object(ai.AI, "getMovesForFoxPiece")
    def test_getAllMovesForPlayer_fox(self, mock_getMovesForFoxPiece):
        """ Get moves for a Fox player """
        mock_getMovesForFoxPiece.return_value = [historynode.HistoryNode()]
        aiObject = ai.AI()
        hnObject = historynode.HistoryNode()
        gooseP = False
        actualValue = len(aiObject.getAllMovesForPlayer(hnObject, gooseP))
        expectedValue = 33
        self.assertEqual(actualValue, expectedValue)

    def test_getCoordinateFromDirection_bad(self):
        """ Test error is raised for direction that doesn't exist """
        testLocation = coordinate.Coordinate(5, 4)
        self.assertRaises(ValueError,
                          ai.getCoordinateFromDirection,
                          testLocation,
                          10)

    def test_getCoordinateFromDirection_good(self):
        """ Test successfully getting coordinate from direction """
        test_xBoard = 6
        test_yBoard = 4
        testLocation = coordinate.Coordinate(test_xBoard, test_yBoard)
        result = ai.getCoordinateFromDirection(testLocation, 1)
        result_xBoard = result.get_x_board()
        result_yBoard = result.get_y_board()
        self.assertEqual(test_xBoard, result_xBoard)
        self.assertEqual(test_yBoard + 1, result_yBoard)


    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForGoosePiece_DetailedMoves(self, mock_legalMoveP):
        """ Test that each generated move updates board state correctly """
        mock_legalMoveP.return_value = True
        aiObject = ai.AI()
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(gooseLocation, types.GOOSE)
        resultingMoves = aiObject.getMovesForGoosePiece(hnObject,
                                                        gooseLocation)
        numberOfMoves = len(resultingMoves)
        self.assertEqual(numberOfMoves, 8)
        for direction in range(1, 9):
            move = resultingMoves[direction - 1]
            self.assertEqual(move.getState(gooseLocation), types.EMPTY)
            gooseEnd = ai.getCoordinateFromDirection(gooseLocation, direction)
            errorTemplate = "\nDirection={0}\nxBoard={1}\nyBoard={2}"
            if direction == 6:
                self.assertEqual(move.getState(gooseEnd),
                                 types.SUPERGOOSE,
                                 errorTemplate.format(direction,
                                                      gooseEnd.get_x_board(),
                                                      gooseEnd.get_y_board()))
            else:
                self.assertEqual(move.getState(gooseEnd),
                                 types.GOOSE,
                                 errorTemplate.format(direction,
                                                      gooseEnd.get_x_board(),
                                                      gooseEnd.get_y_board()))

    def test_getMovesForGoosePiece_NotValid(self):
        """ Test finding moves when location isn't a goose. None should be
        found """
        hnObject = historynode.HistoryNode()
        notGooseLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(notGooseLocation, types.FOX)
        aiObject = ai.AI()
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           notGooseLocation))
        self.assertEqual(numberOfMoves, 0)

    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForGoosePiece_NoMoves(self, mock_legalMoveP):
        """ Test finding goose moves when there aren't any """
        mock_legalMoveP.return_value = False
        hnObject = historynode.HistoryNode()
        gooseLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(gooseLocation, types.GOOSE)
        aiObject = ai.AI()
        numberOfMoves = len(aiObject.getMovesForGoosePiece(hnObject,
                                                           gooseLocation))
        self.assertEqual(numberOfMoves, 0)

    def test_getMovesForFoxPiece_NotValid(self):
        """ Test finding moves when location isn't a fox. None should be
        found """
        hnObject = historynode.HistoryNode()
        notFoxLocation = coordinate.Coordinate(6, 4)
        hnObject.setState(notFoxLocation, types.EMPTY)
        aiObject = ai.AI()
        numberOfMoves = len(aiObject.getMovesForFoxPiece(hnObject,
                                                         notFoxLocation))
        self.assertEqual(numberOfMoves, 0)

    @patch.object(ai.AI, "getAllFoxCaptures")
    def test_getMovesForFoxPiece_OnEdge(self, mock_getAllFoxCaptures):
        """ Test finding fox moves on the edge of the board """
        mock_getAllFoxCaptures.return_value = []
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 1)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI()
        actualValue = len(ai_object.getMovesForFoxPiece(hn_object,
                                                        fox_location))
        expectedValue = 3
        self.assertEqual(actualValue, expectedValue)

    @patch.object(ai.AI, "getAllFoxCaptures")
    def test_getMovesForFoxPiece_ExistsCapture(self, mock_getAllFoxCaptures):
        """ Check case when there's at least one capture
        and we return just that """
        mock_getAllFoxCaptures.return_value = ["fake gamenode"]
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI()
        expectedValue = ["fake gamenode"]
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        self.assertEqual(actualValue, expectedValue)

    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForFoxPiece_Good(self, mock_legalMoveP):
        """ Check case when fox move exists and is legal """
        mock_legalMoveP.return_value = True
        hn_object = historynode.HistoryNode()
        ai_object = ai.AI()
        fox_location = coordinate.Coordinate(5, 4)
        hn_object.setState(fox_location, types.FOX)
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        actualValue_inital = actualValue[0].getState(fox_location)
        actualValue_end = actualValue[0].getState(coordinate.Coordinate(5, 5))
        self.assertEqual(len(actualValue), 8)
        self.assertEqual(actualValue_inital, types.EMPTY)
        self.assertEqual(actualValue_end, types.FOX)

    @patch.object(rules.Rules, "legalMoveP")
    def test_getMovesForFoxPiece_none_legal(self, mock_legalMoveP):
        """ Check case when there is no move """
        mock_legalMoveP.return_value = False
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        hn_object.setState(fox_location, types.FOX)
        ai_object = ai.AI()
        actualValue = ai_object.getMovesForFoxPiece(hn_object, fox_location)
        self.assertEqual(len(actualValue), 0) # No legal moves

    def test_getAllFoxCaptures_dir_5(self):
        """ Correctly evaluate a simple game position """
        hn_object = historynode.HistoryNode()
        fox_location = coordinate.Coordinate(3, 4)
        goose_location = coordinate.Coordinate(3, 3)
        hn_object.setState(fox_location, types.FOX)
        hn_object.setState(goose_location, types.GOOSE)
        ai_object = ai.AI()
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
        ai_object = ai.AI()
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
        ai_object = ai.AI()
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1020
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_single_goose(self):
        """ Correctly evaluate a game with a single goose """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 6), types.GOOSE)
        ai_object = ai.AI()
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1018.87
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_single_supergoose(self):
        """ Correctly evaluate a supergoose """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 6), types.SUPERGOOSE)
        ai_object = ai.AI()
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1018
        self.assertAlmostEqual(actualValue, expectedValue)

    def test_evaluationFunction_supergoose_in_fox_area(self):
        """ Correctly evaluate a supergoose in the fox starting area """
        hn_object = historynode.HistoryNode()
        hn_object.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        ai_object = ai.AI()
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = -1015
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
        ai_object = ai.AI()
        actualValue = ai_object.evaluationFunction(hn_object)
        expectedValue = 997.17
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

    def test_getCoordinateHelper_valid(self):
        """ Correctly get a coordinate object from valid coordinates """
        actualValue = ai.getCoordinateHelper(4, 5)
        self.assertIsNotNone(actualValue)

    def test_getCoordinateHelper_invalid(self):
        """ Correctly get None from invalid coordinates """
        actualValue = ai.getCoordinateHelper(7, 7)
        self.assertIsNone(actualValue)
