""" Tests for the Types module """

import unittest

# pylint: disable=import-error
from res import types

class TestTypes(unittest.TestCase):
    """ Tests for the Types module """

    def test_getPieceAbbreviation_empty(self):
        "Correctly convert a type to a character for display"
        self.assertEqual('.', types.getPieceAbbreviation(types.EMPTY))

    def test_getPieceAbbreviation_goose(self):
        "Correctly convert a type to a character for display"
        self.assertEqual('G', types.getPieceAbbreviation(types.GOOSE))

    def test_getPieceAbbreviation_fox(self):
        "Correctly convert a type to a character for display"
        self.assertEqual('F', types.getPieceAbbreviation(types.FOX))

    def test_getPieceAbbreviation_supergoose(self):
        "Correctly convert a type to a character for display"
        self.assertEqual('S', types.getPieceAbbreviation(types.SUPERGOOSE))

    def test_getPieceAbbreviation_outside(self):
        "Correctly convert a type to a character for display"
        self.assertEqual(None, types.getPieceAbbreviation(types.OUTSIDE))

    def test_getPieceAbbreviation_unknown(self):
        "Correctly convert a type to a character for display"
        self.assertRaises(ValueError,
                          types.getPieceAbbreviation,
                          'abcd')
