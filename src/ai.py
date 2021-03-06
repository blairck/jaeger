""" This module contains the AI search algorithm """

from random import shuffle

# pylint: disable=import-error
from res import types
from src import coordinate
from src import historynode
from src import rules

class AI(object):
    """ Class that stores the AI algorithm """
    def __init__(self):
        self.arbiter = rules.Rules()
        self.weightA = 1.0
        self.weightB = 1.0
        self.moveCount = 0

    # pylint: disable=no-member
    def iterativeDeepeningSearch(self, theGame, gooseP, searchPly):
        """ Searches at steadily increasing ply and breaks if a draw or end
        state is found, otherwise searches to searchPly. """
        bestMove = None
        plyRange = range(1, searchPly + 2, 2)
        for ply in plyRange:
            bestMove = self.findBestMove(theGame, gooseP, ply)
            if (bestMove is None
                    or bestMove.score < -999
                    or bestMove.score > 999):
                return bestMove
        return bestMove

    # pylint: disable=too-many-arguments, too-many-branches
    def findBestMove(self,
                     theGame,
                     gooseP,
                     searchPly,
                     minimum=-10000.0,
                     maximum=10000.0,
                     firstCall=True):
        """ Main alpha-beta minimax algorithm to find best move """
        allMoves = self.getAllMovesForPlayer(theGame, gooseP)
        if firstCall and len(allMoves) == 0:
            return None
        elif not firstCall and len(allMoves) == 0:
            return 0.0

        for move in allMoves:
            move.score = self.evaluationFunction(move)
            move.determineWinningState()

        shuffle(allMoves)
        self.moveCount += 1
        searchPly -= 1
        if searchPly > 0 and not theGame.winningState:
            allMoves.sort(key=lambda x: x.score, reverse=gooseP)
            if gooseP:
                for move in allMoves:
                    result = self.findBestMove(move,
                                               not gooseP,
                                               searchPly,
                                               minimum,
                                               maximum,
                                               False)
                    move.score = result
                    if result > minimum:
                        minimum = result
                    if result > maximum:
                        move.score = maximum
                        return move.score
            else:
                for move in allMoves:
                    result = self.findBestMove(move,
                                               not gooseP,
                                               searchPly,
                                               minimum,
                                               maximum,
                                               False)
                    move.score = result
                    if result < maximum:
                        maximum = result
                    if result < minimum:
                        move.score = minimum
                        return move.score
        if firstCall:
            return getHighestOrLowestScoreMove(allMoves, gooseP)
        else:
            return getHighestOrLowestScoreMove(allMoves, gooseP).score

    def getAllMovesForPlayer(self, theGame, gooseP):
        """GooseP == True means it's the Goose player's turn. Otherwise fox"""
        moves = []
        for location in getTupleOfAllCoordinates():
            if gooseP:
                moves.extend(self.getMovesForGoosePiece(theGame, location))
            else:
                moves.extend(self.getMovesForFoxPiece(theGame, location))
        if not gooseP:
            captureMoves = list(filter(lambda x: x.isCapture, moves))
            if len(captureMoves) > 0:
                return captureMoves
        return moves

    def getMovesForGoosePiece(self, theGame, gooseLocation):
        """ This returns a GameNode for every legal move of a given goose """
        moveList = []
        if (theGame.getState(gooseLocation) not in (types.GOOSE,
                                                    types.SUPERGOOSE)):
            # Don't examine a piece that's not a goose or supergoose
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
                moveResult.leafP = True
                moveResult.rootP = False
                moveList.append(moveResult)
        return moveList

    def getMovesForFoxPiece(self, theGame, foxLocation):
        """ Returns a GameNode for every legal move of a given fox. theGame
        is the current board position. """
        moveList = []
        if theGame.getState(foxLocation) != types.FOX:
            # Don't examine a piece that's not a fox
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
                    resultMove.leafP = True
                    resultMove.rootP = False
                    moveList.append(resultMove)
        return moveList

    def getAllFoxCaptures(self, theGame, location):
        """ This recursively finds all available captures for a single fox and
        returns the list of captures. Check for duplicates from loops"""
        tempCaptureList = []
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
                newMoveNode.leafP = True
                newMoveNode.rootP = False
                newMoveNode.isCapture = True
                tempCaptureList.append(newMoveNode)
                nextCapture = self.getAllFoxCaptures(newMoveNode, destination)
                if nextCapture:
                    tempCaptureList.extend(nextCapture)
        captureList = []
        for board in tempCaptureList:
            if board not in captureList:
                captureList.append(board)
        return captureList

    def evaluationFunction(self, theGame, checkForDraw=False):
        """ This function takes a game state and returns a score for the
        position. A positive score favors the geese, and a negative score
        favors the foxes. """
        valueA = 0.0
        valueB = 0.0
        victoryPoints = 0
        totalScore = 0.0

        if checkForDraw:
            if (len(self.getAllMovesForPlayer(theGame, True)) == 0
                    or len(self.getAllMovesForPlayer(theGame, False)) == 0):
                return None

        for x in range(1, 8):
            for y in range(1, 8):
                if theGame.gameState[x - 1][y - 1] == types.GOOSE:
                    # Reward goose player for having material on the board
                    valueA += 1
                    # Reward Goose player for moving to the first row
                    valueA += (7 - y) * 0.1
                    # Reward player slightly for moving to the center column
                    valueA += (4 - abs(4 - x)) * 0.01
                elif theGame.gameState[x - 1][y - 1] == types.SUPERGOOSE:
                    valueA += 2
                    if (3 <= x <= 5
                            and 1 <= y <= 3):
                        # Reward Goose player for occupying victory zone
                        valueB += 4 - y
                        victoryPoints += 1
                elif theGame.gameState[x - 1][y - 1] == types.FOX:
                    # Reward fox player for being near the 1st row
                    valueA -= (7 - y) * 0.2

        valueA -= 20
        valueB *= victoryPoints
        totalScore += self.weightA * valueA + self.weightB * valueB
        if theGame.geeseWinP():
            totalScore += 2000
        elif theGame.foxesWinP():
            totalScore -= 2000

        return totalScore

def getTupleOfAllCoordinates():
    """ Gets a tuple of all legal Coordinates on the board """
    return (coordinate.Coordinate(3, 7), coordinate.Coordinate(4, 7),
            coordinate.Coordinate(5, 7), coordinate.Coordinate(3, 6),
            coordinate.Coordinate(4, 6), coordinate.Coordinate(5, 6),
            coordinate.Coordinate(1, 5), coordinate.Coordinate(2, 5),
            coordinate.Coordinate(3, 5), coordinate.Coordinate(4, 5),
            coordinate.Coordinate(5, 5), coordinate.Coordinate(6, 5),
            coordinate.Coordinate(7, 5), coordinate.Coordinate(1, 4),
            coordinate.Coordinate(2, 4), coordinate.Coordinate(3, 4),
            coordinate.Coordinate(4, 4), coordinate.Coordinate(5, 4),
            coordinate.Coordinate(6, 4), coordinate.Coordinate(7, 4),
            coordinate.Coordinate(1, 3), coordinate.Coordinate(2, 3),
            coordinate.Coordinate(3, 3), coordinate.Coordinate(4, 3),
            coordinate.Coordinate(5, 3), coordinate.Coordinate(6, 3),
            coordinate.Coordinate(7, 3), coordinate.Coordinate(3, 2),
            coordinate.Coordinate(4, 2), coordinate.Coordinate(5, 2),
            coordinate.Coordinate(3, 1), coordinate.Coordinate(4, 1),
            coordinate.Coordinate(5, 1))

def transferNode(startNode):
    """ Copies input historynode to a new one and returns that.
    Basically performs a deep copy."""
    endNode = historynode.HistoryNode()
    for x in range(0, 7):
        for y in range(0, 7):
            endNode.gameState[x][y] = startNode.gameState[x][y]
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

def getHighestOrLowestScoreMove(moves, gooseP):
    """ Returns the highest/lowest scored move depending on the player """
    if gooseP:
        return max(moves, key=lambda x: x.score)
    else:
        return min(moves, key=lambda x: x.score)
