""" This module contains the AI search algorithm """

from src import coordinate
from src import historynode

class AI(object):
    """AI class"""
    def transferNode(self, startNode):
        """ Copies input historynode to a new one and returns that """
        endNode = historynode.HistoryNode()
        for x in range (7):
            for y in range(7):
                try:
                    location = coordinate.Coordinate(x+1, y+1)
                except ValueError:
                    continue
                state = startNode.getState(location);
                endNode.setState(location, state)
        return endNode