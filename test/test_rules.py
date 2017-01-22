""" Tests for the rules module """

import unittest
from src import coordinate
from src import gamenode
from src import rules

class TestRules(unittest.TestCase):
    """ Tests for the rules module """

    def test_makeCapture_horizontal(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 4)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When
        rules_obj.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_vertical(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(4, 4)
        captureCoordinate = coordinate.Coordinate(4, 5)
        endCoordinate = coordinate.Coordinate(4, 6)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When
        rules_obj.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_diagonal(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 5)
        endCoordinate = coordinate.Coordinate(5, 6)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When
        rules_obj.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_horizontal_bad_x(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(6, 4)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When/Assert
        self.assertRaises(ValueError,
                          rules_obj.makeCapture,
                          board,
                          startCoordinate,
                          endCoordinate)

    def test_makeCapture_horizontal_bad_y(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        captureCoordinate = coordinate.Coordinate(3, 5)
        endCoordinate = coordinate.Coordinate(3, 6)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When/Assert
        self.assertRaises(ValueError,
                          rules_obj.makeCapture,
                          board,
                          startCoordinate,
                          endCoordinate)

    def test_makeCapture_horizontal_same_coordinates(self):
        # Given
        board = gamenode.GameNode()
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        captureCoordinate = coordinate.Coordinate(3, 5)
        board.setState(startCoordinate, 2) # Make a fox piece
        board.setState(captureCoordinate, 1) # Make a goose piece

        # When/Assert
        self.assertRaises(ValueError,
                          rules_obj.makeCapture,
                          board,
                          startCoordinate,
                          startCoordinate)

    def test_findDirection_1(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(5, 7)
        expected_result = 1
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_2(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(7, 7)
        expected_result = 2
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_3(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(7, 5)
        expected_result = 3
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_4(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(7, 3)
        expected_result = 4
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_5(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(5, 3)
        expected_result = 5
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_6(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 3)
        expected_result = 6
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_7(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 5)
        expected_result = 7
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_8(self):
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 7)
        expected_result = 8
        actual_result = rules_obj.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_convertCharToInt_good_value_1(self):
        """ Test a known good value"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('1')
        self.assertEqual(result, 1)

    def test_convertCharToInt_good_value_3(self):
        """ Test a known good value"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('3')
        self.assertEqual(result, 3)

    def test_convertCharToInt_upper_value_10(self):
        """ Test a value that should be too high"""
        rules_obj = rules.Rules()
        self.assertRaises(ValueError, rules_obj.convertCharToInt, '10')

    def test_convertCharToInt_lower_value_5(self):
        """ Test a value that should be too low"""
        rules_obj = rules.Rules()
        self.assertRaises(ValueError, rules_obj.convertCharToInt, '-5')

    def test_convertCharToInt_bad_value(self):
        """ Test a value that isn't an int"""
        rules_obj = rules.Rules()
        self.assertRaises(ValueError, rules_obj.convertCharToInt, 'qq')
