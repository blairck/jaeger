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

    def findDirection(self, startCoordinate, endCoordinate):
        startX = startCoordinate.get_x_array()
        startY = startCoordinate.get_y_array()
        endX = endCoordinate.get_x_array()
        endY = endCoordinate.get_y_array()
        differenceX = endX - startX
        differenceY = endY - startY

        if differenceX == 0 and differenceY == 2:
            return 1
        elif differenceX == 2 and differenceY == 2:
            return 2
        elif differenceX == 2 and differenceY == 0:
            return 3
        elif differenceX == 2 and differenceY == -2:
            return 4
        elif differenceX == 0 and differenceY == -2:
            return 5
        elif differenceX == -2 and differenceY == -2:
            return 6
        elif differenceX == -2 and differenceY == 0:
            return 7
        elif differenceX == -2 and differenceY == 2:
            return 8
        else:
            error_template = ("findDirection() unable to resolve coordinates: "
                              "Start - ({0}, {1}), End - ({2}, {3})")
            raise ValueError(error_template.format(startX, startY, endX, endY))

    def convertCharToInt(self, value):
        """ Converts a string of length 1 (char) to an int. """
        try:
            value = int(value)
        except ValueError:
            error_template = ("convertCharToInt received '{0}' when num "
                              "expected")
            raise ValueError(error_template.format(value))
        if value > 9 or value < 0:
            error_template = "Value larger or smaller than 1 digit: {0}"
            raise ValueError(error_template.format(value))
        return value
