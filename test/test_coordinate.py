import unittest
from src import coordinate

class TestRules(unittest.TestCase):
    """ Tests for the coordinate module """

    def test_get_x_board(self):
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 4
        actual_result = board_location.get_x_board()
        self.assertEqual(actual_result, expected_result)

    def test_get_y_board(self):
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 6
        actual_result = board_location.get_y_board()
        self.assertEqual(actual_result, expected_result)

    def test_get_x_array(self):
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 3
        actual_result = board_location.get_x_array()
        self.assertEqual(actual_result, expected_result)

    def test_get_y_array(self):
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 5
        actual_result = board_location.get_y_array()
        self.assertEqual(actual_result, expected_result)

    def test_coordinate_bad_x(self):
        self.assertRaises(TypeError, coordinate.Coordinate, "4", 6)

    def test_coordinate_bad_y(self):
        self.assertRaises(TypeError, coordinate.Coordinate, 4, "6")

    def test_coordinate_bad_location(self):
        self.assertRaises(ValueError, coordinate.Coordinate, 50, 100)
