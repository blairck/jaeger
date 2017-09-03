""" This module contains the AI search algorithm """

import operator

# pylint: disable=import-error
from res import types
from src import coordinate
from src import historynode
from src import rules

class AI(object):
    """ Class that stores the AI algorithm """
    def __init__(self, a, b):
        self.arbiter = rules.Rules()
        self.weightA = a
        self.weightB = b
        self.moveCount = 0

    def findBestMove_DEPRECATED(self,
                     theGame,
                     gooseP,
                     searchPly):
        allMoves = self.getAllMovesForPlayer(theGame, gooseP)
        numberOfMoves = len(allMoves)
        self.moveCount += 1
        searchPly -= 1
        if searchPly > 0:
            for move in allMoves:
                if not move.winningState:
                    result = self.findBestMove(move,
                                               not gooseP,
                                               searchPly).score
                    move.score = result
        if numberOfMoves > 0:
            return self.getHighestOrLowestScoreMove(allMoves, gooseP)
        else:
            return 0.0

    def findBestMove(self,
                     theGame,
                     gooseP,
                     searchPly,
                     minimum=-10000,
                     maximum=10000):
        allMoves = self.getAllMovesForPlayer(theGame, gooseP)
        self.moveCount += 1
        searchPly -= 1
        if searchPly > 0 and not theGame.winningState:
            if gooseP:
                for move in allMoves:
                    result = self.findBestMove(move,
                                               not gooseP,
                                               searchPly,
                                               minimum,
                                               maximum).score
                    move.score = result
                    if result > minimum:
                        minimum = result
                    if result > maximum:
                        move.score = maximum
                        return move
            else:
                for move in allMoves:
                    result = self.findBestMove(move,
                                               not gooseP,
                                               searchPly,
                                               minimum,
                                               maximum).score
                    move.score = result
                    if result < maximum:
                        maximum = result
                    if move.score < minimum:
                        move.score = minimum
                        return move
        return self.getHighestOrLowestScoreMove(allMoves, gooseP)

    def getHighestOrLowestScoreMove(self, moves, gooseP):
        """ Returns the highest/lowest scored move depending on the player """
        if gooseP:
            return max(moves, key=lambda x: x.score)
        else:
            return min(moves, key=lambda x: x.score)

    def getAllMovesForPlayer(self, theGame, gooseP):
        """GooseP == True means it's the Goose player's turn. Otherwise fox"""
        moves = []
        for x in range(1, 9):
            for y in range(1, 9):
                location = getCoordinateHelper(x, y)
                if not location:
                    continue
                if gooseP:
                    moves.extend(self.getMovesForGoosePiece(theGame, location))
                else:
                    moves.extend(self.getMovesForFoxPiece(theGame, location))
        return moves

    def getMovesForGoosePiece(self, theGame, gooseLocation):
        """ This returns a GameNode for every legal move of a given goose """
        moveList = []
        if (theGame.getState(gooseLocation) not in (types.GOOSE,
                                                    types.SUPERGOOSE)):
            """ Don't examine a piece that's not a goose or supergoose """
            return moveList

        for direction in range(1, 9):
            gooseDestination = getCoordinateFromDirection(gooseLocation,
                                                          direction)
            if (gooseDestination and
                    self.arbiter.legalMoveP(theGame,
                                            gooseLocation,
                                            gooseDestination)):
                gooseType = theGame.getState(gooseLocation)
                moveResult = transferNode(theGame)
                finalGooseType = rules.resultingGoose(gooseType,
                                                      gooseDestination)
                moveResult.setState(gooseDestination, finalGooseType)
                moveResult.setState(gooseLocation, types.EMPTY)
                moveResult.score = self.evaluationFunction(moveResult)
                moveResult.determineWinningState()
                moveResult.leafP = True
                moveResult.rootP = False
                moveList.append(moveResult)
        return moveList

    def getMovesForFoxPiece(self, theGame, foxLocation):
        """ Returns a GameNode for every legal move of a given fox. theGame
        is the current board position. """
        moveList = []
        if theGame.getState(foxLocation) != types.FOX:
            """ Don't examine a piece that's not a fox """
            return moveList
        moveList = self.getAllFoxCaptures(theGame, foxLocation)

        if len(moveList) == 0:
            # These are regular non-capture moves for the fox, if no captures
            # were found
            for direction in range(1, 9):
                foxDestination = getCoordinateFromDirection(foxLocation,
                                                            direction)
                if (foxDestination and
                        self.arbiter.legalMoveP(theGame,
                                                foxLocation,
                                                foxDestination)):
                    resultMove = transferNode(theGame)
                    resultMove.setState(foxDestination, types.FOX)
                    resultMove.setState(foxLocation, types.EMPTY)
                    resultMove.score = self.evaluationFunction(resultMove)
                    resultMove.determineWinningState()
                    resultMove.leafP = True
                    resultMove.rootP = False
                    moveList.append(resultMove)
        return moveList

    def getAllFoxCaptures(self, theGame, location):
        """ This recursively finds all available captures for a single fox and
        returns the list of captures"""
        captureList = []
        x_board = location.get_x_board()
        y_board = location.get_y_board()
        for direction in range(1, 9):
            if self.arbiter.isACaptureP(theGame, location, direction):
                deltaX = rules.findXCoordinateFromDirection(direction)
                deltaY = rules.findYCoordinateFromDirection(direction)
                newMoveNode = transferNode(theGame)
                destination = coordinate.Coordinate(x_board + deltaX,
                                                    y_board + deltaY)
                rules.makeCapture(newMoveNode, location, destination)
                newMoveNode.score = self.evaluationFunction(newMoveNode)
                newMoveNode.determineWinningState()
                newMoveNode.leafP = True
                newMoveNode.rootP = False
                captureList.append(newMoveNode)
                nextCapture = self.getAllFoxCaptures(newMoveNode, destination)
                if nextCapture:
                    captureList.extend(nextCapture)
        return captureList

    def evaluationFunction(self, theGame):
        """ This function takes a game state and returns a score for the
        position. A positive score favors the geese, and a negative score
        favors the foxes. """
        valueA = 0.0
        valueB = 0.0
        victoryPoints = 0
        totalScore = 0.0

        for x in range(1, 8):
            for y in range(1, 8):
                try:
                    location = coordinate.Coordinate(x, y)
                except ValueError:
                    continue
                if theGame.getState(location) == types.GOOSE:
                    valueA += 1
                elif theGame.getState(location) == types.SUPERGOOSE:
                    valueA += 2
                    if 3 <= x <= 5 and 1 <= y <= 3:
                        valueB += 4 - y
                        victoryPoints += 1

        valueA -= 20
        valueB *= victoryPoints
        totalScore += self.weightA * valueA + self.weightB * valueB
        #self.evaluated += 1
        if theGame.geeseWinP():
            totalScore += 1000
        elif theGame.foxesWinP():
            totalScore -= 1000

        return totalScore

def transferNode(startNode):
    """ Copies input historynode to a new one and returns that.
    Basically performs a deep copy."""
    endNode = historynode.HistoryNode()
    for x in range(1, 8):
        for y in range(1, 8):
            try:
                location = coordinate.Coordinate(x, y)
            except ValueError:
                continue
            state = startNode.getState(location)
            endNode.setState(location, state)
    return endNode

# pylint: disable=too-many-return-statements
def getCoordinateFromDirection(currentLocation, direction):
    """ Gets a coordinate delta from a current one & direction """

    xBoard = currentLocation.get_x_board()
    yBoard = currentLocation.get_y_board()

    if direction == 1:
        return getCoordinateHelper(xBoard, yBoard + 1)
    elif direction == 2:
        return getCoordinateHelper(xBoard + 1, yBoard + 1)
    elif direction == 3:
        return getCoordinateHelper(xBoard + 1, yBoard)
    elif direction == 4:
        return getCoordinateHelper(xBoard + 1, yBoard - 1)
    elif direction == 5:
        return getCoordinateHelper(xBoard, yBoard - 1)
    elif direction == 6:
        return getCoordinateHelper(xBoard - 1, yBoard - 1)
    elif direction == 7:
        return getCoordinateHelper(xBoard - 1, yBoard)
    elif direction == 8:
        return getCoordinateHelper(xBoard - 1, yBoard + 1)
    else:
        raise ValueError

def getCoordinateHelper(xBoard, yBoard):
    """ Wrap the error handling """
    try:
        return coordinate.Coordinate(xBoard, yBoard)
    except ValueError:
        return None
