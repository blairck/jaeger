""" This module contains the AI search algorithm """

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

    def getAllFoxCaptures(self, theGame, location):
        """ This recursively finds all available captures for a single fox and
        returns the list of captures"""
        if not self.arbiter.existsCaptureAtLocationP(theGame, location):
            return None
        captureList = []
        x_board = location.get_x_board()
        y_board = location.get_y_board()
        for direction in range(1, 9):
            if self.arbiter.isACaptureP(theGame, location, direction):
                deltaX = rules.findXCoordinateFromDirection(direction)
                deltaY = rules.findYCoordinateFromDirection(direction)
                moveState = transferNode(theGame)
                destination = coordinate.Coordinate(x_board + deltaX,
                                                    y_board + deltaY)
                rules.makeCapture(moveState, location, destination)
                singleMove = transferNode(moveState)
                singleMove.score = self.evaluationFunction(moveState)
                singleMove.leafP = True
                singleMove.rootP = False
                captureList.append(singleMove)
                nextCapture = self.getAllFoxCaptures(moveState, destination)
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
    """ Copies input historynode to a new one and returns that """
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
