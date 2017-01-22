""" This module contains rules to the game."""

from src import coordinate

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""
    def makeCapture(self, theGame, startCoordinate, endCoordinate):
        startX = startCoordinate.get_x_board()
        startY = startCoordinate.get_y_board()
        endX = endCoordinate.get_x_board()
        endY = endCoordinate.get_y_board()
        if abs(startX - endX) not in (0, 2):
            error_template = "Illegal X capture: {0} -> {1}"
            raise ValueError(error_template.format(startX, endX))
        elif abs(startY - endY) not in (0, 2):
            error_template = "Illegal Y capture: {0} -> {1}"
            raise ValueError(error_template.format(startY, endY))
        elif startX == endX and startY == endY:
            error_template = ("Start and end capture coordinates are the "
                              "same: ({0}, {1})")
            raise ValueError(error_template.format(startX, startY))

        captureStartX = int(startX + (endX - startX)/2)
        captureStartY = int(startY + (endY - startY)/2)
        captureCoordinate = coordinate.Coordinate(captureStartX, captureStartY)

        theGame.setState(startCoordinate, 0)
        theGame.setState(captureCoordinate, 0)
        theGame.setState(endCoordinate, 2)


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
