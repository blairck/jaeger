""" This module contains the AI search algorithm """

from src import coordinate
from src import historynode

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
