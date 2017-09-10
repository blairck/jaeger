""" This module contains the interface for playing the game """

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode

class Interface(object):
    """ Class that stores UI helper functions """
    def __init__(self):
        pass

def getPositionFromListOfMoves(theMoves, userInput, gooseP):
    # Todo write implementation
    pass

def getCoordinatesFromUserInput(userInput):
    result = []
    userInput = ''.join(c for c in userInput if c.isdigit())
    inputLength = len(userInput)
    if inputLength < 2 or inputLength % 2 == 1:
        return []
    try:
        result.append(coordinate.Coordinate(int(userInput[0]),
                                            int(userInput[1])))
        for i in range(2, inputLength, 2):
            result.append(coordinate.Coordinate(int(userInput[i]),
                                                int(userInput[i+1])))
    except ValueError:
        return []
    return result