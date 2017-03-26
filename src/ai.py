""" This module contains the AI search algorithm """

from res import types
from src import coordinate
from src import historynode

class AI(object):
    """ Class that stores the AI algorithm """
    def __init__(self, a, b):
        self.weightA = a
        self.weightB = b

    # This function takes a game state and returns a score for the position.
    # A positive score favors the geese, and a negative score favors the foxes.
    def evaluationFunction(self, theGame):
        valueA = 0.0
        valueB = 0.0
        victoryPoints = 0
        totalScore = 0.0

        for x in range(1,8):
            for y in range(1,8):
                try:
                    location = coordinate.Coordinate(x, y)
                except ValueError:
                    continue
                if theGame.getState(location) == types.GOOSE:
                    valueA += 1
                elif theGame.getState(location) == types.SUPERGOOSE:
                    valueA += 2
                    if 3<=x<=5 and 1<=y<=3:
                        valueB += 4 - y
                        victoryPoints += 1

        valueA -= 20
        valueB *= victoryPoints
        totalScore += self.weightA * valueA + self.weightB * valueB
        #TODO fix this
        #self.evaluated += 1
        if theGame.geeseWinP():
            totalScore += 1000
        elif theGame.foxesWinP():
            totalScore -= 1000

        return totalScore

def transferNode(startNode):
    """ Copies input historynode to a new one and returns that """
    endNode = historynode.HistoryNode()
    for x in range (1, 8):
        for y in range(1, 8):
            try:
                location = coordinate.Coordinate(x, y)
            except ValueError:
                continue
            state = startNode.getState(location);
            endNode.setState(location, state)
    return endNode
