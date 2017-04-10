""" This module contains rules to the game."""

# pylint: disable=import-error
from res import types
from src import connection
from src import coordinate
from src import historynode

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        if not test_mode:
            path = "res/board_connections.txt"
            self.boardConnections = self.readConnectionFile(path)

    def readConnectionFile(self, file_path, test_data=None):
        """ Reads in the file of connections """
        result = []
        with open(file_path) as f:
            if test_data and self.test_mode:
                f = test_data
            for line in f:
                result.append(parseConnectionLine(line))
        return result

    def readGameFile(self, file_path, test_data=None):
        """ Reads in saved game file """
        result = []
        with open(file_path) as f:
            if test_data and self.test_mode:
                f = test_data
            for line in f:
                result.append(line)
        return result

    # pylint: disable=too-many-locals, too-many-statements
    def readSavedFile(self, path_string, test_data=None):
        """ Reads a saved game file and processes the contents into metadata
        and game nodes """
        savedGameMoveStates = []
        allLinedStrings = None
        metadata = None
        if test_data:
            allLinedStrings = test_data
            metadata = allLinedStrings.pop(0)
        else:
            allLinedStrings = self.readGameFile(path_string)
            metadata = makeMetadata(allLinedStrings)
            allLinedStrings = allLinedStrings[7:]
        savedGameMoveStates.append(metadata)
        allLinedStrings = list(zip(*(iter(allLinedStrings),)*8))
        p1Name = "{0}".format(metadata['p1'])
        p2Name = "{0}".format(metadata['p2'])
        result = "{0}".format(metadata['re'])
        gameType = "{0}".format(metadata['gt'])
        gooseSearch = "{0}".format(metadata['gs'])
        foxSearch = "{0}".format(metadata['fs'])
        for turn in allLinedStrings:
            nextNode = historynode.HistoryNode()
            nextNode.setP1(p1Name)
            nextNode.setP2(p2Name)
            nextNode.setResult(result)
            nextNode.setGameType(int(gameType))
            nextNode.setGooseSearch(int(gooseSearch))
            nextNode.setFoxSearch(int(foxSearch))
            nextNode.setHalfMove(int(turn[0][4]))

            coordinate_3 = coordinate.Coordinate(3, 7)
            coordinate_4 = coordinate.Coordinate(4, 7)
            coordinate_5 = coordinate.Coordinate(5, 7)
            nextNode.setState(coordinate_3, int(turn[1][4]))
            nextNode.setState(coordinate_4, int(turn[1][6]))
            nextNode.setState(coordinate_5, int(turn[1][8]))

            coordinate_3 = coordinate.Coordinate(3, 6)
            coordinate_4 = coordinate.Coordinate(4, 6)
            coordinate_5 = coordinate.Coordinate(5, 6)
            nextNode.setState(coordinate_3, int(turn[2][4]))
            nextNode.setState(coordinate_4, int(turn[2][6]))
            nextNode.setState(coordinate_5, int(turn[2][8]))

            coordinate_1 = coordinate.Coordinate(1, 5)
            coordinate_2 = coordinate.Coordinate(2, 5)
            coordinate_3 = coordinate.Coordinate(3, 5)
            coordinate_4 = coordinate.Coordinate(4, 5)
            coordinate_5 = coordinate.Coordinate(5, 5)
            coordinate_6 = coordinate.Coordinate(6, 5)
            coordinate_7 = coordinate.Coordinate(7, 5)
            nextNode.setState(coordinate_1, int(turn[3][0]))
            nextNode.setState(coordinate_2, int(turn[3][2]))
            nextNode.setState(coordinate_3, int(turn[3][4]))
            nextNode.setState(coordinate_4, int(turn[3][6]))
            nextNode.setState(coordinate_5, int(turn[3][8]))
            nextNode.setState(coordinate_6, int(turn[3][10]))
            nextNode.setState(coordinate_7, int(turn[3][12]))

            coordinate_1 = coordinate.Coordinate(1, 4)
            coordinate_2 = coordinate.Coordinate(2, 4)
            coordinate_3 = coordinate.Coordinate(3, 4)
            coordinate_4 = coordinate.Coordinate(4, 4)
            coordinate_5 = coordinate.Coordinate(5, 4)
            coordinate_6 = coordinate.Coordinate(6, 4)
            coordinate_7 = coordinate.Coordinate(7, 4)
            nextNode.setState(coordinate_1, int(turn[4][0]))
            nextNode.setState(coordinate_2, int(turn[4][2]))
            nextNode.setState(coordinate_3, int(turn[4][4]))
            nextNode.setState(coordinate_4, int(turn[4][6]))
            nextNode.setState(coordinate_5, int(turn[4][8]))
            nextNode.setState(coordinate_6, int(turn[4][10]))
            nextNode.setState(coordinate_7, int(turn[4][12]))

            coordinate_1 = coordinate.Coordinate(1, 3)
            coordinate_2 = coordinate.Coordinate(2, 3)
            coordinate_3 = coordinate.Coordinate(3, 3)
            coordinate_4 = coordinate.Coordinate(4, 3)
            coordinate_5 = coordinate.Coordinate(5, 3)
            coordinate_6 = coordinate.Coordinate(6, 3)
            coordinate_7 = coordinate.Coordinate(7, 3)
            nextNode.setState(coordinate_1, int(turn[5][0]))
            nextNode.setState(coordinate_2, int(turn[5][2]))
            nextNode.setState(coordinate_3, int(turn[5][4]))
            nextNode.setState(coordinate_4, int(turn[5][6]))
            nextNode.setState(coordinate_5, int(turn[5][8]))
            nextNode.setState(coordinate_6, int(turn[5][10]))
            nextNode.setState(coordinate_7, int(turn[5][12]))

            coordinate_3 = coordinate.Coordinate(3, 2)
            coordinate_4 = coordinate.Coordinate(4, 2)
            coordinate_5 = coordinate.Coordinate(5, 2)
            nextNode.setState(coordinate_3, int(turn[6][4]))
            nextNode.setState(coordinate_4, int(turn[6][6]))
            nextNode.setState(coordinate_5, int(turn[6][8]))

            coordinate_3 = coordinate.Coordinate(3, 1)
            coordinate_4 = coordinate.Coordinate(4, 1)
            coordinate_5 = coordinate.Coordinate(5, 1)
            nextNode.setState(coordinate_3, int(turn[7][4]))
            nextNode.setState(coordinate_4, int(turn[7][6]))
            nextNode.setState(coordinate_5, int(turn[7][8]))

            savedGameMoveStates.append(nextNode)
        return savedGameMoveStates

    def findConnectionP(self, startCoordinate, endCoordinate):
        """Finds connection between start coordinate and end coordinate.
        Returns True if connection exists, False otherwise"""
        startX = startCoordinate.get_x_board()
        startY = startCoordinate.get_y_board()
        endX = endCoordinate.get_x_board()
        endY = endCoordinate.get_y_board()
        for con in self.boardConnections:
            if (con.startX == startX and
                    con.startY == startY and
                    con.endX == endX and
                    con.endY == endY):
                return True
        return False

    def legalMoveP(self, theGame, startCoordinate, endCoordinate):
        """"Tests whether a start coordinate and end coordinate constitute a
        legal move"""
        if (theGame.getState(startCoordinate) == types.GOOSE and
                endCoordinate.get_y_board() > startCoordinate.get_y_board()):
            return False
        elif (theGame.getState(endCoordinate) == types.EMPTY and
              self.findConnectionP(startCoordinate, endCoordinate)):
            return True
        return False

    def captureHelper(self,
                      theGame,
                      foxCoordinate,
                      delta_mid,
                      delta_end):
        """ Determines if a particular set up board + fox + delta
        constitutes a legal capture """
        x = foxCoordinate.get_x_board()
        y = foxCoordinate.get_y_board()
        try:
            middle_coordinate = coordinate.Coordinate(x+delta_mid['x'],
                                                      y+delta_mid['y'])
            end_coordinate = coordinate.Coordinate(x+delta_end['x'],
                                                   y+delta_end['y'])
        except ValueError:
            # Sometimes delta coordinates will result in a position off the
            # board. In these cases, just return False since no capture is
            # possible here.
            return False
        middle_tile_state = theGame.getState(middle_coordinate)
        end_tile_state = theGame.getState(end_coordinate)
        return bool((middle_tile_state in (types.GOOSE, types.SUPERGOOSE)) and
                    end_tile_state == 0 and
                    self.findConnectionP(middle_coordinate, end_coordinate))

    def isACaptureP(self, theGame, foxCoordinate, direction):
        """Returns true if there's a capture, given a fox coordinate and
        a direction. otherwise returns false"""
        delta_mid = None
        delta_end = None
        if direction == 1 and foxCoordinate.get_y_board() < 6:
            delta_mid = {'x':0, 'y':1}
            delta_end = {'x':0, 'y':2}
        elif (direction == 2 and
              foxCoordinate.get_x_board() < 6 and
              foxCoordinate.get_y_board() < 6):
            delta_mid = {'x':1, 'y':1}
            delta_end = {'x':2, 'y':2}
        elif direction == 3 and foxCoordinate.get_x_board() < 6:
            delta_mid = {'x':1, 'y':0}
            delta_end = {'x':2, 'y':0}
        elif (direction == 4 and
              foxCoordinate.get_x_board() < 6 and
              foxCoordinate.get_y_board() > 2):
            delta_mid = {'x':1, 'y':-1}
            delta_end = {'x':2, 'y':-2}
        elif direction == 5 and foxCoordinate.get_y_board() > 2:
            delta_mid = {'x':0, 'y':-1}
            delta_end = {'x':0, 'y':-2}
        elif (direction == 6 and
              foxCoordinate.get_x_board() > 2 and
              foxCoordinate.get_y_board() > 2):
            delta_mid = {'x':-1, 'y':-1}
            delta_end = {'x':-2, 'y':-2}
        elif (direction == 7 and
              foxCoordinate.get_x_board() > 2):
            delta_mid = {'x':-1, 'y':0}
            delta_end = {'x':-2, 'y':0}
        elif (direction == 8 and
              foxCoordinate.get_x_board() > 2 and
              foxCoordinate.get_y_board() < 6):
            delta_mid = {'x':-1, 'y':1}
            delta_end = {'x':-2, 'y':2}

        if delta_mid and delta_end:
            return self.captureHelper(theGame,
                                      foxCoordinate,
                                      delta_mid,
                                      delta_end)
        else:
            # Fox is near the edge of the board and won't be able to capture
            # in this direction.
            return False

    def existsCaptureAtLocationP(self, theGame, location):
        """ Returns bool if a capture exists at a location on the board """
        for direction in range(1, 9):
            if self.isACaptureP(theGame, location, direction):
                return True
        return False

    def existsCaptureP(self, theGame):
        """ Returns true if the foxes can make a capture, false otherwise """
        firstP = True
        foxOne = None
        foxTwo = None

        for i in range(1, 8):
            for j in range(1, 8):
                try:
                    location = coordinate.Coordinate(i, j)
                except ValueError:
                    # Don't need to check tiles that are off the board
                    continue
                if firstP and theGame.getState(location) == 2:
                    foxOne = coordinate.Coordinate(i, j)
                    firstP = False
                elif not firstP and theGame.getState(location) == 2:
                    foxTwo = coordinate.Coordinate(i, j)
                    break

        if None in (foxOne, foxTwo):
            error_template = ("Didn't find both foxes on the board. This "
                              "should never happen.")
            raise ValueError(error_template)

        for direction in range(1, 8):
            if self.isACaptureP(theGame, foxOne, direction):
                return True
            if self.isACaptureP(theGame, foxTwo, direction):
                return True
        return False

# Static functions
def makeCapture(theGame, startCoordinate, endCoordinate):
    """ Update the board for a capture between a start + end
    coordinates """
    startX = startCoordinate.get_x_board()
    startY = startCoordinate.get_y_board()
    endX = endCoordinate.get_x_board()
    endY = endCoordinate.get_y_board()

    if abs(startX - endX) not in (0, 2):
        error_template = "Illegal X capture: {0} -> {1}"
        raise ValueError(error_template.format(startX, endX))
    elif abs(startY - endY) not in (0, 2):
        error_template = "Illegal Y capture: {0} -> {1}"
        raise ValueError(error_template.format(startY, endY))
    elif startX == endX and startY == endY:
        error_template = ("Start and end capture coordinates are the "
                          "same: ({0}, {1})")
        raise ValueError(error_template.format(startX, startY))

    captureStartX = int(startX + (endX - startX)/2)
    captureStartY = int(startY + (endY - startY)/2)
    captureCoordinate = coordinate.Coordinate(captureStartX, captureStartY)

    theGame.setState(startCoordinate, 0)
    theGame.setState(captureCoordinate, 0)
    theGame.setState(endCoordinate, 2)

# pylint: disable=too-many-return-statements
def findDirection(startCoordinate, endCoordinate):
    """ Find the direction between two adjacent coordinates """
    startX = startCoordinate.get_x_array()
    startY = startCoordinate.get_y_array()
    endX = endCoordinate.get_x_array()
    endY = endCoordinate.get_y_array()
    differenceX = endX - startX
    differenceY = endY - startY

    if differenceX == 0 and differenceY == 2:
        return 1
    elif differenceX == 2 and differenceY == 2:
        return 2
    elif differenceX == 2 and differenceY == 0:
        return 3
    elif differenceX == 2 and differenceY == -2:
        return 4
    elif differenceX == 0 and differenceY == -2:
        return 5
    elif differenceX == -2 and differenceY == -2:
        return 6
    elif differenceX == -2 and differenceY == 0:
        return 7
    elif differenceX == -2 and differenceY == 2:
        return 8
    else:
        error_template = ("findDirection() unable to resolve coordinates: "
                          "Start - ({0}, {1}), End - ({2}, {3})")
        raise ValueError(error_template.format(startX, startY, endX, endY))

def parseConnectionLine(line):
    """ Parse a connection line and return the result.
    Used as a map for connections between all tiles on the board."""
    result = connection.Connection()
    result.setstartX(int(line[0]))
    result.setstartY(int(line[2]))
    result.setdirection(int(line[4]))
    result.setendX(int(line[6]))
    result.setendY(int(line[8]))
    return result

def convertCharToInt(value):
    """ Converts a string of length 1 (char) to an int. """
    try:
        value = int(value)
    except ValueError:
        error_template = ("convertCharToInt received '{0}' when num "
                          "expected")
        raise ValueError(error_template.format(value))
    if value > 9 or value < 0:
        error_template = "Value larger or smaller than 1 digit: {0}"
        raise ValueError(error_template.format(value))
    return value

def resultingGoose(currentType, gooseCoordinate):
    """ This returns a supergoose when a goose moves into the fox area (for
    use in the AI algorithm) """
    if ((3 <= gooseCoordinate.get_x_board() <= 5) and
            (1 <= gooseCoordinate.get_y_board() <= 3)):
        return 3
    else:
        return currentType

def findXCoordinateFromDirection(direction):
    """ Returns delta X, when given a direction value """
    if direction in (1, 5):
        return 0
    elif direction in (2, 3, 4):
        return 2
    elif direction in (6, 7, 8):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template)

def findYCoordinateFromDirection(direction):
    """ Returns delta Y, when given a direction value """
    if direction in (3, 7):
        return 0
    elif direction in (8, 1, 2):
        return 2
    elif direction in (4, 5, 6):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template)

def makeMetadata(linedStrings):
    """ Makes a metadata dictionary from the saved game file """
    result = {}
    value = linedStrings[0][4:].strip('\n')
    result["{0}{1}".format(linedStrings[0][0],
                           linedStrings[0][1])] = value
    value = linedStrings[1][4:].strip('\n')
    result["{0}{1}".format(linedStrings[1][0],
                           linedStrings[1][1])] = value
    value = linedStrings[2][4:].strip('\n')
    result["{0}{1}".format(linedStrings[2][0],
                           linedStrings[2][1])] = value
    value = linedStrings[3][4:].strip('\n')
    result["{0}{1}".format(linedStrings[3][0],
                           linedStrings[3][1])] = value
    value = linedStrings[4][4:].strip('\n')
    result["{0}{1}".format(linedStrings[4][0],
                           linedStrings[4][1])] = value
    value = linedStrings[5][4:].strip('\n')
    result["{0}{1}".format(linedStrings[5][0],
                           linedStrings[5][1])] = value
    value = linedStrings[6][4:].strip('\n')
    result["{0}{1}".format(linedStrings[6][0],
                           linedStrings[6][1])] = value
    return result

# pylint: disable=too-many-statements
def saveGame(game_turns, metadata):
    """ Game_turns is a list of gamenodes. This returns a string
    representation (human readable) of the game thus far. """
    fileContents = ""
    halfMove = 0
    fileContents = "{0}{1}".format(fileContents,
                                   "p1: {0}\n".format(metadata['p1']))
    fileContents = "{0}{1}".format(fileContents,
                                   "p2: {0}\n".format(metadata['p2']))
    fileContents = "{0}{1}".format(fileContents,
                                   "re: {0}\n".format(metadata['re']))
    fileContents = "{0}{1}".format(fileContents,
                                   "gt: {0}\n".format(metadata['gt']))
    fileContents = "{0}{1}".format(fileContents,
                                   "gs: {0}\n".format(metadata['gs']))
    fileContents = "{0}{1}".format(fileContents,
                                   "fs: {0}\n".format(metadata['fs']))

    for turn in game_turns:
        halfMove += 1

        fileContents = "{0}{1}".format(fileContents,
                                       "hm: {0}\n".format(halfMove))

        coordinate_3 = coordinate.Coordinate(3, 7)
        coordinate_4 = coordinate.Coordinate(4, 7)
        coordinate_5 = coordinate.Coordinate(5, 7)
        line = "    {0} {1} {2}    \n".format(turn.getState(coordinate_3),
                                              turn.getState(coordinate_4),
                                              turn.getState(coordinate_5))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_3 = coordinate.Coordinate(3, 6)
        coordinate_4 = coordinate.Coordinate(4, 6)
        coordinate_5 = coordinate.Coordinate(5, 6)
        line = "    {0} {1} {2}    \n".format(turn.getState(coordinate_3),
                                              turn.getState(coordinate_4),
                                              turn.getState(coordinate_5))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_1 = coordinate.Coordinate(1, 5)
        coordinate_2 = coordinate.Coordinate(2, 5)
        coordinate_3 = coordinate.Coordinate(3, 5)
        coordinate_4 = coordinate.Coordinate(4, 5)
        coordinate_5 = coordinate.Coordinate(5, 5)
        coordinate_6 = coordinate.Coordinate(6, 5)
        coordinate_7 = coordinate.Coordinate(7, 5)
        line_template = "{0} {1} {2} {3} {4} {5} {6}\n"
        line = line_template.format(turn.getState(coordinate_1),
                                    turn.getState(coordinate_2),
                                    turn.getState(coordinate_3),
                                    turn.getState(coordinate_4),
                                    turn.getState(coordinate_5),
                                    turn.getState(coordinate_6),
                                    turn.getState(coordinate_7))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_1 = coordinate.Coordinate(1, 4)
        coordinate_2 = coordinate.Coordinate(2, 4)
        coordinate_3 = coordinate.Coordinate(3, 4)
        coordinate_4 = coordinate.Coordinate(4, 4)
        coordinate_5 = coordinate.Coordinate(5, 4)
        coordinate_6 = coordinate.Coordinate(6, 4)
        coordinate_7 = coordinate.Coordinate(7, 4)
        line_template = "{0} {1} {2} {3} {4} {5} {6}\n"
        line = line_template.format(turn.getState(coordinate_1),
                                    turn.getState(coordinate_2),
                                    turn.getState(coordinate_3),
                                    turn.getState(coordinate_4),
                                    turn.getState(coordinate_5),
                                    turn.getState(coordinate_6),
                                    turn.getState(coordinate_7))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_1 = coordinate.Coordinate(1, 3)
        coordinate_2 = coordinate.Coordinate(2, 3)
        coordinate_3 = coordinate.Coordinate(3, 3)
        coordinate_4 = coordinate.Coordinate(4, 3)
        coordinate_5 = coordinate.Coordinate(5, 3)
        coordinate_6 = coordinate.Coordinate(6, 3)
        coordinate_7 = coordinate.Coordinate(7, 3)
        line_template = "{0} {1} {2} {3} {4} {5} {6}\n"
        line = line_template.format(turn.getState(coordinate_1),
                                    turn.getState(coordinate_2),
                                    turn.getState(coordinate_3),
                                    turn.getState(coordinate_4),
                                    turn.getState(coordinate_5),
                                    turn.getState(coordinate_6),
                                    turn.getState(coordinate_7))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_3 = coordinate.Coordinate(3, 2)
        coordinate_4 = coordinate.Coordinate(4, 2)
        coordinate_5 = coordinate.Coordinate(5, 2)
        line = "    {0} {1} {2}    \n".format(turn.getState(coordinate_3),
                                              turn.getState(coordinate_4),
                                              turn.getState(coordinate_5))
        fileContents = "{0}{1}".format(fileContents, line)

        coordinate_3 = coordinate.Coordinate(3, 1)
        coordinate_4 = coordinate.Coordinate(4, 1)
        coordinate_5 = coordinate.Coordinate(5, 1)
        line = "    {0} {1} {2}    \n".format(turn.getState(coordinate_3),
                                              turn.getState(coordinate_4),
                                              turn.getState(coordinate_5))
        fileContents = "{0}{1}".format(fileContents, line)
    return fileContents
