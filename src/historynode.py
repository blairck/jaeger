""" Stores board state with additional game specific logic """

from res import types
from src import gamenode
from src import helper

class HistoryNode(gamenode.GameNode):
    """ Class that inherits from GameNode and has additional game specific
    logic """

    # pylint: disable=too-many-instance-attributes
    # Ten is reasonable for the current version

    def __init__(self):
        super(HistoryNode, self).__init__()
        self.result = None # int
        self.gameType = None # int
        self.foxSearch = None # int
        self.gooseSearch = None # int
        self.halfMove = None # int
        self.p1 = None # str
        self.p2 = None # str
        self.winningState = False

    def print_board(self):
        print("Player 1: {0}".format(self.p1))
        print("Player 2: {0}".format(self.p2))
        print("Result: {0}".format(self.result))
        print("Game Type: {0}".format(self.gameType))
        print("Fox Search: {0}".format(self.foxSearch))
        print("Goose Search: {0}".format(self.gooseSearch))
        print("Half Move: {0}".format(self.halfMove))
        print("    {0} {1} {2}    ".format(self.gameState[2][6],
                                           self.gameState[3][6],
                                           self.gameState[4][6]))
        print("    {0} {1} {2}    ".format(self.gameState[2][5],
                                           self.gameState[3][5],
                                           self.gameState[4][5]))
        self.print_middle_rows(" ")
        print("    {0} {1} {2}    ".format(self.gameState[2][1],
                                           self.gameState[3][1],
                                           self.gameState[4][1]))
        print("    {0} {1} {2}    ".format(self.gameState[2][0],
                                           self.gameState[3][0],
                                           self.gameState[4][0]))

    def constructor(self):
        """ Sets up the internal state of the HistoryNode instance """
        self.score = 0.0
        self.winningState = False
        self.rootP = True

        self.result = 0
        self.gameType = 1
        self.foxSearch = 1
        self.gooseSearch = 1
        self.halfMove = 1

        self.gameState[0][0] = -1
        self.gameState[0][1] = -1
        self.gameState[1][0] = -1
        self.gameState[1][1] = -1
        self.gameState[0][5] = -1
        self.gameState[0][6] = -1
        self.gameState[1][5] = -1
        self.gameState[1][6] = -1
        self.gameState[5][0] = -1
        self.gameState[5][1] = -1
        self.gameState[6][0] = -1
        self.gameState[6][1] = -1
        self.gameState[5][5] = -1
        self.gameState[5][6] = -1
        self.gameState[6][5] = -1
        self.gameState[6][6] = -1

        for j in range(2, 7):
            for i in range(0, 7):
                if j == 2 and i >= 2 and i <= 4:
                    continue
                if j >= 5 and (i < 2 or i > 4):
                    continue
                self.gameState[i][j] = 1

        self.gameState[2][0] = 2
        self.gameState[4][0] = 2

    def setP1(self, a_string):
        """ Setter for P1 with type checking """
        if not isinstance(a_string, str):
            raise TypeError(("a_string is not a string. "
                             "a_string = {0}").format(a_string))
        self.p1 = a_string

    def setP2(self, a_string):
        """ Setter for P2 with type checking """
        if not isinstance(a_string, str):
            raise TypeError(("a_string is not a string. "
                             "a_string = {0}").format(a_string))
        self.p2 = a_string

    def geeseWinP(self):
        """ Returns True if the geese have won, false otherwise """
        foxSpacesOccupied = 0
        for i in range(2, 5):
            for j in range(0, 3):
                if self.gameState[i][j] == 1 or self.gameState[i][j] == 3:
                    foxSpacesOccupied += 1
                    if foxSpacesOccupied == 9:
                        # Geese win
                        return True
        # Geese haven't won yet
        return False

    def foxesWinP(self):
        """ Returns True if the foxes have won, false otherwise """
        geeseRemaining = 0
        for i in range(0, 7):
            for j in range(0, 7):
                if (self.gameState[i][j] == types.GOOSE or
                    self.gameState[i][j] == types.SUPERGOOSE):
                    geeseRemaining += 1
                    # Too many geese, foxes have not won yet
                    if geeseRemaining >= 9:
                        return False
        # Geese have insufficient material, Foxes win
        return True

    def setGameType(self, value):
        """ Setter for gameType with type checking """
        helper.checkIfInt(value)
        self.gameType = value

    def setFoxSearch(self, value):
        """ Setter for foxSearch with type checking """
        helper.checkIfInt(value)
        self.foxSearch = value

    def setResult(self, value):
        """ Setter for result with type checking """
        #helper.checkIfInt(value)
        self.result = value

    def setGooseSearch(self, value):
        """ Setter for gooseSearch with type checking """
        helper.checkIfInt(value)
        self.gooseSearch = value

    def setHalfMove(self, value):
        """ Setter for halfMove with type checking """
        helper.checkIfInt(value)
        self.halfMove = value

    def determineWinningState(self):
        """ Set winningState if this node is in one """
        if (self.geeseWinP() or self.foxesWinP()):
            self.winningState = True
        else:
            self.winningState = False
