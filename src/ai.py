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

    def getMovesForGoosePiece(theGame, gooseLocation):
        """ This returns a GameNode for every legal move of a given goose """
        xBoard = gooseLocation.get_x_board()
        yBoard = gooseLocation.get_y_board()
        moveList = []

        # Direction 1
        gooseDestination = coordinate.Coordinate(xBoard, yBoard + 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 2
        gooseDestination = coordinate.Coordinate(xBoard + 1, yBoard + 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 3
        gooseDestination = coordinate.Coordinate(xBoard + 1, yBoard)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 4
        gooseDestination = coordinate.Coordinate(xBoard + 1, yBoard - 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 5
        gooseDestination = coordinate.Coordinate(xBoard, yBoard - 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 6
        gooseDestination = coordinate.Coordinate(xBoard - 1, yBoard - 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 7
        gooseDestination = coordinate.Coordinate(xBoard - 1, yBoard)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass
        # Direction 8
        gooseDestination = coordinate.Coordinate(xBoard - 1, yBoard + 1)
        if self.arbiter.legalMoveP(theGame, gooseLocation, gooseDestination):
            pass


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
        moveState = transferNode(theGame)
        moveState.setState(foxDestination, types.FOX)
        moveState.setState(foxLocation, types.EMPTY)
        singleMove = transferNode(moveState)
        singleMove.score = self.evaluationFunction(moveState)
        singleMove.leafP = True
        singleMove.rootP = False
        return singleMove

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
