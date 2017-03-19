""" Tests for the AI module """

import unittest

from res import types
from src import ai
from src import coordinate
from src import historynode

class TestRules(unittest.TestCase):
    """ Tests for the AI module """

    def test_transferNode(self):
        """ Correctly transfer a historynode """
        hn_object = historynode.HistoryNode()
        location = coordinate.Coordinate(3, 3)
        hn_object.setState(location, types.SUPERGOOSE)
        result = ai.transferNode(hn_object)
        actualValue = result.getState(location)
        expectedValue = types.SUPERGOOSE
        self.assertEqual(actualValue, expectedValue)
