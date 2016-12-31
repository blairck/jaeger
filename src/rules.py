""" This module contains rules to the game."""

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""
    def __init__(self, debug=False):
        self.debug = debug

    def makeCapture(self, theGame, startX, startY, endX, endY):
        theGame.setState(startX-1, startY-1, 0)
        theGame.setState((startX-1)+((endX-1)-(startX-1))/2,
                         (startY-1)+((endY-1)-(startY-1))/2,
                         0)
        theGame.setState(endX-1, endY-1, 2)

    def convertCharToInt(self, value):
        """ Converts a string of length 1 (char) to an int. This has an
        intentional return of 0 if the input is non-int. """
        try:
            value = int(value)
            if value > 9 or value < 1:
                value = 0
        except ValueError:
            if self.debug:
                message = "convertCharToInt received '{0}' when num expected"
                print(message.format(value))
            value = 0
        return value
