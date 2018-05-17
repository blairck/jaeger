""" Stores board state with additional game specific logic """

# pylint: disable=import-error
from res import types
from src import gamenode

from settings import ALPHABETNOTATION

class HistoryNode(gamenode.GameNode):
    """ Class that inherits from GameNode and has additional game specific
    logic """

    def __init__(self):
        super(HistoryNode, self).__init__()
        # Jaeger settings
        self.isCapture = False
        self.winningState = False
        self.foxesWin = None
        self.geeseWin = None

    def __eq__(self, other):
        for i in range(0, 7):
            for j in range(0, 7):
                if self.gameState[i][j] != other.gameState[i][j]:
                    return False
        return True

    def print_board(self):
        """ Prints a simplified representation of the board """
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

    def pretty_print_board(self):
        """ Prints the board state in a way that is easier to understand """
        print("7         {0} - {1} - {2}".format(
            types.getPieceAbbreviation(self.gameState[2][6]),
            types.getPieceAbbreviation(self.gameState[3][6]),
            types.getPieceAbbreviation(self.gameState[4][6])))
        print(r"          | \ | / |")
        print("6         {0} - {1} - {2}".format(
            types.getPieceAbbreviation(self.gameState[2][5]),
            types.getPieceAbbreviation(self.gameState[3][5]),
            types.getPieceAbbreviation(self.gameState[4][5])))
        print(r"          | / | \ |")
        print("5 {0} - {1} - {2} - {3} - {4} - {5} - {6}".format(
            types.getPieceAbbreviation(self.gameState[0][4]),
            types.getPieceAbbreviation(self.gameState[1][4]),
            types.getPieceAbbreviation(self.gameState[2][4]),
            types.getPieceAbbreviation(self.gameState[3][4]),
            types.getPieceAbbreviation(self.gameState[4][4]),
            types.getPieceAbbreviation(self.gameState[5][4]),
            types.getPieceAbbreviation(self.gameState[6][4])))
        print(r"  | \ | / | \ | / | \ | / |")
        print("4 {0} - {1} - {2} - {3} - {4} - {5} - {6}".format(
            types.getPieceAbbreviation(self.gameState[0][3]),
            types.getPieceAbbreviation(self.gameState[1][3]),
            types.getPieceAbbreviation(self.gameState[2][3]),
            types.getPieceAbbreviation(self.gameState[3][3]),
            types.getPieceAbbreviation(self.gameState[4][3]),
            types.getPieceAbbreviation(self.gameState[5][3]),
            types.getPieceAbbreviation(self.gameState[6][3])))
        print(r"  | / | \ | / | \ | / | \ |")
        print("3 {0} - {1} - {2} - {3} - {4} - {5} - {6}".format(
            types.getPieceAbbreviation(self.gameState[0][2]),
            types.getPieceAbbreviation(self.gameState[1][2]),
            types.getPieceAbbreviation(self.gameState[2][2]),
            types.getPieceAbbreviation(self.gameState[3][2]),
            types.getPieceAbbreviation(self.gameState[4][2]),
            types.getPieceAbbreviation(self.gameState[5][2]),
            types.getPieceAbbreviation(self.gameState[6][2])))
        print(r"          | \ | / |")
        print("2         {0} - {1} - {2}".format(
            types.getPieceAbbreviation(self.gameState[2][1]),
            types.getPieceAbbreviation(self.gameState[3][1]),
            types.getPieceAbbreviation(self.gameState[4][1])))
        print(r"          | / | \ |")
        print("1         {0} - {1} - {2}".format(
            types.getPieceAbbreviation(self.gameState[2][0]),
            types.getPieceAbbreviation(self.gameState[3][0]),
            types.getPieceAbbreviation(self.gameState[4][0])))
        if ALPHABETNOTATION:
            print("  A   B   C   D   E   F   G")
        else:
            print("  1   2   3   4   5   6   7")

    def constructor(self):
        """ Sets up the internal state of the HistoryNode instance """
        self.score = 0.0
        self.winningState = False
        self.rootP = True

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

    def geeseWinP(self):
        """ Returns True if the geese have won, false otherwise """
        if self.geeseWin is None:
            foxSpacesOccupied = 0
            for i in range(2, 5):
                for j in range(0, 3):
                    if self.gameState[i][j] == 1 or self.gameState[i][j] == 3:
                        foxSpacesOccupied += 1
                        if foxSpacesOccupied == 9:
                            # Geese win
                            self.geeseWin = True
                            return self.geeseWin
            # Geese haven't won yet
            self.geeseWin = False
        return self.geeseWin

    def foxesWinP(self):
        """ Returns True if the foxes have won, false otherwise.
        The result is cached with the historynode. """
        if self.foxesWin is None:
            geeseRemaining = 0
            for i in range(0, 7):
                for j in range(0, 7):
                    if (self.gameState[i][j] == types.GOOSE
                            or self.gameState[i][j] == types.SUPERGOOSE):
                        geeseRemaining += 1
                        # Too many geese, foxes have not won yet
                        if geeseRemaining >= 9:
                            self.foxesWin = False
                            return self.foxesWin
            # Geese have insufficient material, Foxes win
            self.foxesWin = True
        return self.foxesWin

    def determineWinningState(self):
        """ Set winningState if this node is in one """
        self.winningState = bool(self.geeseWinP() or self.foxesWinP())
