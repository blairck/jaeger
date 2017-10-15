""" This module contains the interface for playing the game """

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import historynode

def getPositionFromListOfMoves(theMoves, userInput, gooseP):
    """ Gets a position with userInput from a list of legal moves (theMoves).
    Returns empty list if none found or ambiguous"""
    userCoordinates = getCoordinatesFromUserInput(userInput)
    if len(userCoordinates) == 1:
        return matchSingleCoordinateToMoves(theMoves,
                                            userCoordinates[0],
                                            gooseP)
    elif len(userCoordinates) > 1:
        return matchMultipleCoordinatesToMoves(theMoves,
                                               userCoordinates,
                                               gooseP)
    else:
        return []

def matchSingleCoordinateToMoves(theMoves, userCoordinate, gooseP):
    """ Match user input when there's only one legal move """
    result = list(filter(lambda x: isCoordinateMatch(x,
                                                     userCoordinate,
                                                     gooseP), theMoves))
    return result

def matchMultipleCoordinatesToMoves(theMoves, userCoordinates, gooseP):
    """ Match user input when there are multiple legal moves """
    lastCoordinate = userCoordinates.pop()
    for coordinate in userCoordinates:
        """ Filters moves by empty spaces in user input"""
        theMoves = list(filter(lambda x: x.getState(coordinate)==types.EMPTY,
                               theMoves))
    theMoves = matchSingleCoordinateToMoves(theMoves, lastCoordinate, gooseP)
    return theMoves

def isCoordinateMatch(theMove, userCoordinate, gooseP):
    """ Returns true or false if the user coordinate matches theMove """
    destinationType = theMove.getState(userCoordinate)
    if gooseP and destinationType in (types.GOOSE, types.SUPERGOOSE):
        return True
    if not gooseP and destinationType is types.FOX:
        return True
    else:
        return False

def getCoordinatesFromUserInput(userInput):
    """ Parses string of user input to get coordinates """
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
