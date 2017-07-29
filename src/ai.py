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

    def getMovesForGoosePiece(self, theGame, gooseLocation):
        """ This returns a GameNode for every legal move of a given goose """
        xBoard = gooseLocation.get_x_board()
        yBoard = gooseLocation.get_y_board()
        moveList = []

        # Direction 1
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard,
                                                                  yBoard + 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 2
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard + 1,
                                                                  yBoard + 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 3
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard + 1,
                                                                  yBoard)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 4
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard + 1,
                                                                  yBoard - 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 5
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard,
                                                                  yBoard - 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 6
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard - 1,
                                                                  yBoard - 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 7
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard - 1,
                                                                  yBoard)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))
        # Direction 8
        gDestination = self.getMovesForGoosePieceCoordinateHelper(xBoard - 1,
                                                                  yBoard + 1)
        if (gDestination and
            self.arbiter.legalMoveP(theGame, gooseLocation, gDestination)):
            moveList.append(self.getMovesForGoosePieceHelper(theGame,
                                                             gooseLocation,
                                                             gDestination))

        return moveList

    def getMovesForGoosePieceHelper(self,
                                    theGame,
                                    gooseLocation,
                                    gooseDestination):
        gooseType = theGame.getState(gooseLocation)
        newMoveNode = transferNode(theGame)
        newMoveNode.setState(gooseDestination, gooseType)
        newMoveNode.setState(gooseLocation, types.EMPTY)
        newMoveNode.score = self.evaluationFunction(newMoveNode)
        newMoveNode.leafP = True
        newMoveNode.rootP = False
        return newMoveNode

    def getMovesForGoosePieceCoordinateHelper(self, xBoard, yBoard):
        try:
            return coordinate.Coordinate(xBoard, yBoard)
        except ValueError:
            return None

#   Direction 3
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+1])
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x+1 :y :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         [moveList addObject: singleMove]; 
#   Direction 4
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y])
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x+1 :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y-1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         [moveList addObject: singleMove]; 
#   Direction 5
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y])
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x: y-1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         [moveList addObject: singleMove]; 
#   Direction 6
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y])
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x-1 :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y-1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         [moveList addObject: singleMove]; 
#   Direction 7
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+1])
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x-1 :y :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         [moveList addObject: singleMove]; 

#     //only check these following situations for supergeese (game[x][y]==3)
#   Direction 8
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+2] && [theGame getState:x :y]==3)
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x-1 :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y+1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         //[singleMove print];
#         [moveList addObject: singleMove]; 
#   Direction 1
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y+2] && [theGame getState:x :y]==3)
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x: y+1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         //[singleMove print];
#         [moveList addObject: singleMove]; 
#   Direction 2
#     if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+2] && [theGame getState:x :y]==3)
#         HistoryNode *singleMove = [HistoryNode new];
#         [self transferNode: theGame: moveState];
#         [moveState setState:x+1 :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y+1]];
#         [moveState setState:x :y :0];
#         [singleMove initialize];
#         [self transferNode:moveState :singleMove];
#         [singleMove setScore:[self evaluationFunction:moveState]];
#         [singleMove setLeafP: TRUE];
#         [singleMove setRootP: FALSE];
#         //[singleMove print];
#         [moveList addObject: singleMove]; 

#     return moveList;

    def getMovesForFoxPiece(self, theGame, foxLocation):
        """ Returns a GameNode for every legal move of a given fox. theGame
        is the current board position. """
        x_board = foxLocation.get_x_board()
        y_board = foxLocation.get_y_board()
        moveList = self.getAllFoxCaptures(theGame, foxLocation)

        if len(moveList) == 0:
            # These are regular non-capture moves for the fox, and no captures
            # were found
            # Direction 1
            foxDestination = coordinate.Coordinate(x_board, y_board + 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 2
            foxDestination = coordinate.Coordinate(x_board + 1, y_board + 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 3
            foxDestination = coordinate.Coordinate(x_board + 1, y_board)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 4
            foxDestination = coordinate.Coordinate(x_board + 1, y_board - 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 5
            foxDestination = coordinate.Coordinate(x_board, y_board - 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 6
            foxDestination = coordinate.Coordinate(x_board - 1, y_board - 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 7
            foxDestination = coordinate.Coordinate(x_board - 1, y_board)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))
            # Direction 8
            foxDestination = coordinate.Coordinate(x_board - 1, y_board + 1)
            if self.arbiter.legalMoveP(theGame, foxLocation, foxDestination):
                moveList.append(self.getMovesForFoxPieceHelper(theGame,
                                                               foxLocation,
                                                               foxDestination))

        return moveList

    def getMovesForFoxPieceHelper(self, theGame, foxLocation, foxDestination):
        """ Return the new GameNode based on the fox's move """
        newMoveNode = transferNode(theGame)
        newMoveNode.setState(foxDestination, types.FOX)
        newMoveNode.setState(foxLocation, types.EMPTY)
        newMoveNode.score = self.evaluationFunction(newMoveNode)
        newMoveNode.leafP = True
        newMoveNode.rootP = False
        return newMoveNode

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
