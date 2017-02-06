""" This module contains rules to the game."""

from res import types
from src import connection
from src import coordinate

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        if not test_mode:
            self.boardConnections = self.readFile("board_connections.txt")

    def makeCapture(self, theGame, startCoordinate, endCoordinate):
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

    def findDirection(self, startCoordinate, endCoordinate):
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

    def parseConnectionLine(self, line):
        result = connection.Connection()
        result.setstartX(int(line[0]))
        result.setstartY(int(line[2]))
        result.setdirection(int(line[4]))
        result.setendX(int(line[6]))
        result.setendY(int(line[8]))
        return result

    def readFile(self, file_name, test_data=None):
        """ Reads in the file of connections """
        file_path = "res/{0}".format(file_name)
        result = []
        with open(file_path) as f:
            if test_data and self.test_mode:
                f = test_data
            for line in f:
                result.append(self.parseConnectionLine(line))
        return result

    def findConnectionP(self, startCoordinate, endCoordinate):
        """Finds connection between start coordinate and end coordinate.
        Returns True if connection exists, False otherwise"""
        startX = startCoordinate.get_x_board()
        startY = startCoordinate.get_y_board()
        endX = endCoordinate.get_x_board()
        endY = endCoordinate.get_y_board()
        for connection in self.boardConnections:
            if (connection.startX == startX and
                connection.startY == startY and
                connection.endX == endX and
                connection.endY == endY):
                return True
        return False

    def legalMoveP(self, theGame, startCoordinate, endCoordinate):
        """"Tests whether a start coordinate and end coordinate constitute a
        legal move"""
        if (theGame.getState(startCoordinate)==types.GOOSE and
            endCoordinate.get_y_board()>startCoordinate.get_y_board()):
            return False
        elif (theGame.getState(endCoordinate)==types.EMPTY and
              self.findConnectionP(startCoordinate, endCoordinate)):
            return True
        return False

    # "Returns true if there's a capture, given a fox coordinate and a direction. otherwise returns false"
    # -(bool)isACaptureP: (GameNode *) theGame: (int) foxX: (int) foxY: (int) direction
    # {
    #     foxX-=1;
    #     foxY-=1;

    #     int game[7][7];
    #     for (int i=0;i<7;i++)
    #      {
    #         for (int j=0;j<7;j++)
    #          {
    #             game[i][j]=[theGame getState:i :j];
    #          }
    #      }

    #     if (direction==1 && foxY<5 &&
    #             (game[foxX][foxY+1]==1 || game[foxX][foxY+1]==3) && game[foxX][foxY+2]==0 &&
    #             [self findConnectionP:foxX+1 :foxY+2 :foxX+1 :foxY+3])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 1.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==2 && foxX<5 && foxY<5 &&
    #              (game[foxX+1][foxY+1]==1 || game[foxX+1][foxY+1]==3) && game[foxX+2][foxY+2]==0 &&
    #              [self findConnectionP:foxX+2 :foxY+2 :foxX+3 :foxY+3])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 2.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==3 && foxX<5 &&
    #              (game[foxX+1][foxY]==1 || game[foxX+1][foxY]==3) && game[foxX+2][foxY]==0 &&
    #              [self findConnectionP:foxX+2 :foxY+1 :foxX+3 :foxY+1])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 3.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==4 && foxX<5 && foxY>1 &&
    #              (game[foxX+1][foxY-1]==1 || game[foxX+1][foxY-1]==3) && game[foxX+2][foxY-2]==0 &&
    #              [self findConnectionP:foxX+2 :foxY :foxX+3 :foxY-1])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 4.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==5 && foxY>1 &&
    #              (game[foxX][foxY-1]==1 || game[foxX][foxY-1]==3) && game[foxX][foxY-2]==0 &&
    #              [self findConnectionP:foxX+1 :foxY :foxX+1 :foxY-1])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 5.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==6 && foxX>1 && foxY>1 &&
    #              (game[foxX-1][foxY-1]==1 || game[foxX-1][foxY-1]==3) && game[foxX-2][foxY-2]==0 &&
    #              [self findConnectionP:foxX :foxY :foxX-1 :foxY-1])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 6.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==7 && foxX>1 &&
    #              (game[foxX-1][foxY]==1 || game[foxX-1][foxY]==3) && game[foxX-2][foxY]==0 &&
    #              [self findConnectionP:foxX :foxY+1 :foxX-1 :foxY+1])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 7.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else if (direction==8 && foxX>1 && foxY<5 &&
    #              (game[foxX-1][foxY+1]==1 || game[foxX-1][foxY+1]==3) && game[foxX-2][foxY+2]==0 &&
    #              [self findConnectionP:foxX :foxY+2 :foxX-1 :foxY+3])
    #      {
    #         //NSLog(@"The fox at %i,%i can capture in direction 8.", foxX, foxY);
    #         return TRUE;
    #      }
    #     else
    #      {
    #         return FALSE;
    #      }
    # }

    # def existsCaptureP(self, theGame):
    #     """ Returns true if the foxes can make a capture, false otherwise """
    #     raise NotImplementedError("TODO - Finish this")
    #     firstP = True
    #     foxOneX = -1
    #     foxOneY = -1
    #     foxTwoX = -1
    #     foxTwoY = -1

    #     for (int i=0; i<7; i++):
    #         for (int j=0;j<7;j++):
    #             if (firstP && [theGame getState:i :j] == 2):
    #                 foxOneX = i
    #                 foxOneY = j
    #                 firstP = False
    #             else if (!firstP && [theGame getState:i :j] == 2):
    #                 foxTwoX = i
    #                 foxTwoY = j
    #                 break

    #     if (-1 in (foxOneX, foxOneY, foxTwoX, foxTwoY)):
    #         error_template = "Didn't find both foxes on the board"
    #         raise ValueError(error_template)

    #     for (int i=1; i<=8; i++):
    #         if ([self isACaptureP: theGame: foxOneX+1: foxOneY+1: i]):
    #             # "Fox One can capture"
    #             return True
    #         if ([self isACaptureP: theGame: foxTwoX+1: foxTwoY+1: i]):
    #             # "Fox Two can capture.
    #             return True
    #     return False

    def convertCharToInt(self, value):
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
