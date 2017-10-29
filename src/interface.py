""" This module contains the interface for playing the game """

# pylint: disable=import-error
from res import types
from src import coordinate

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
    for aCoordinate in userCoordinates:
        # Filters moves by empty spaces in user input
        theMoves = list(
            filter(lambda x, c=aCoordinate: x.getState(c) == types.EMPTY,
                   theMoves))
    theMoves = matchSingleCoordinateToMoves(theMoves, lastCoordinate, gooseP)
    return theMoves

def isCoordinateMatch(theMove, userCoordinate, gooseP):
    """ Returns true or false if the user coordinate matches theMove """
    destinationType = theMove.getState(userCoordinate)
    if gooseP and destinationType in (types.GOOSE, types.SUPERGOOSE):
        return True
    return bool(not gooseP and destinationType is types.FOX)

def parseAlphabetNotation(userInput):
    """ Replaces any valid coordinate character with a number """
    userInput = userInput.lower()
    userInput = userInput.replace("a", "1")
    userInput = userInput.replace("b", "2")
    userInput = userInput.replace("c", "3")
    userInput = userInput.replace("d", "4")
    userInput = userInput.replace("e", "5")
    userInput = userInput.replace("f", "6")
    userInput = userInput.replace("g", "7")
    return userInput

def getCoordinatesFromUserInput(userInput):
    """ Parses string of user input to get coordinates """
    result = []
    userInput = parseAlphabetNotation(userInput)
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
