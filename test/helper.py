""" Helper functions for unit tests """

from contextlib import contextmanager
from io import StringIO
import sys

from res import types
from src import historynode
from src import coordinate

# 7         S - . - .
#           | \ | / |
# 6         S - . - .
#           | / | \ |
# 5 . - . - . - . - . - . - .
#   | \ | / | \ | / | \ | / |
# 4 . - . - . - . - S - . - .
#   | / | \ | / | \ | / | \ |
# 3 . - . - S - S - S - . - .
#           | \ | / |
# 2         S - S - ~
#           | / | \ |
# 1         F - F - S
#   1   2   3   4   5   6   7
nearlyDrawnGame = historynode.HistoryNode()
nearlyDrawnGame.setState(coordinate.Coordinate(3, 1), types.FOX)
nearlyDrawnGame.setState(coordinate.Coordinate(4, 1), types.FOX)
nearlyDrawnGame.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(5, 4), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(3, 3), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(3, 6), types.SUPERGOOSE)
nearlyDrawnGame.setState(coordinate.Coordinate(3, 7), types.SUPERGOOSE)

# 7         . - . - .
#           | \ | / |
# 6         . - . - .
#           | / | \ |
# 5 . - G - . - . - . - . - F
#   | \ | / | \ | / | \ | / |
# 4 . - . - . - . - . - . - F
#   | / | \ | / | \ | / | \ |
# 3 . - . - ~ - S - S - . - .
#           | \ | / |
# 2         S - S - S
#           | / | \ |
# 1         S - S - S
#   1   2   3   4   5   6   7
# Goose to play. Best move is G25-G24...G24-S33#
nearlyWonGooseGame = historynode.HistoryNode()
nearlyWonGooseGame.setState(coordinate.Coordinate(7, 4), types.FOX)
nearlyWonGooseGame.setState(coordinate.Coordinate(7, 5), types.FOX)
nearlyWonGooseGame.setState(coordinate.Coordinate(2, 5), types.GOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)
nearlyWonGooseGame.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)

# 7         G - G - G
#           | \ | / |
# 6         . - . - .
#           | / | \ |
# 5 . - . - S - . - G - . - G
#   | \ | / | \ | / | \ | / |
# 4 . - . - . - . - . - . - G
#   | / | \ | / | \ | / | \ |
# 3 . - . - G - . - S - . - G
#           | \ | / |
# 2         . - F - .
#           | / | \ |
# 1         . - F - .
#   1   2   3   4   5   6   7
loopedFoxCapture = historynode.HistoryNode()
loopedFoxCapture.setState(coordinate.Coordinate(3, 7), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(4, 7), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(5, 7), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(3, 5), types.SUPERGOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(5, 5), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(7, 5), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(7, 4), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(3, 3), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(7, 3), types.GOOSE)
loopedFoxCapture.setState(coordinate.Coordinate(4, 2), types.FOX)
loopedFoxCapture.setState(coordinate.Coordinate(4, 1), types.FOX)

@contextmanager
def captured_output():
    """ Redirects stdout to StringIO so we can inspect Print statements """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out
