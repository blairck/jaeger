""" Integration tests for the rules module """

import unittest

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode
from src import rules

class TestIntegRules(unittest.TestCase):
    """ Integration tests for the rules module """
    def test_isACaptureP_direction_4(self):
        """ IsACaptureP calls direction with a move that doesn't exist """
        direction = 4
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 4)
        goose_location = coordinate.Coordinate(4, 3)
        board.setState(foxCoordinate, types.FOX)
        board.setState(goose_location, types.GOOSE)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_existsCaptureP_capture(self):
        """ End to end test for finding a real goose capture """
        rules_obj = rules.Rules()
        foxOne = coordinate.Coordinate(5, 5)
        foxTwo = coordinate.Coordinate(3, 7)
        goose = coordinate.Coordinate(4, 5)
        board = gamenode.GameNode()
        board.setState(foxOne, types.FOX)
        board.setState(foxTwo, types.FOX)
        board.setState(goose, types.GOOSE)
        actual_result = rules_obj.existsCaptureP(board)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
