""" Tests for the rules module """

import unittest
from src import rules

class TestRules(unittest.TestCase):
    """ Tests for the rules module """

    def test_good_value_1(self):
        """ Test a known good value"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('1')
        self.assertEqual(result, 1)

    def test_good_value_3(self):
        """ Test a known good value"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('3')
        self.assertEqual(result, 3)

    def test_upper_value_10(self):
        """ Test a value that should be too high"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('10')
        self.assertEqual(result, 0)

    def test_lower_value_5(self):
        """ Test a value that should be too low"""
        rules_obj = rules.Rules()
        result = rules_obj.convertCharToInt('-5')
        self.assertEqual(result, 0)

    def test_bad_value(self):
        """ Test a value that isn't an int"""
        rules_obj = rules.Rules(debug=True)
        result = rules_obj.convertCharToInt('qq')
        self.assertEqual(result, 0)
