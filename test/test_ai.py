""" Tests for the AI module """

import unittest

from src import ai

class TestRules(unittest.TestCase):
    """ Tests for the AI module """

    def test_transferNode(self):
        """ Correctly transfer a historynode """
        ai_object = ai.AI()
        actualValue = ai_object.transferNode(1)
        expectedValue = True
        self.assertEqual(actualValue, expectedValue)