from src import gamenode

class HistoryNode(gamenode.GameNode):
    def __init__(self):
        super(HistoryNode, self).__init__()
        self.result = None # int
        self.gameType = None # int
        self.foxSearch = None # int
        self.gooseSearch = None # int
        self.halfMove = None # int
        self.p1 = None # str
        self.p2 = None # str

    def print_board(self):
        print("Player 1: {0}".format(self.p1))
        print("Player 2: {0}".format(self.p2))
        print("Result: {0}".format(self.result))
        print("Game Type: {0}".format(self.gameType))
        print("Fox Search: {0}".format(self.foxSearch))
        print("Goose Search: {0}".format(self.gooseSearch))
        print("Half Move: {0}".format(self.halfMove))
        print("      {0} {1} {2}      ".format(self.gameState[2][6],
                                               self.gameState[3][6],
                                               self.gameState[4][6]))
        print("      {0} {1} {2}      ".format(self.gameState[2][5],
                                               self.gameState[3][5],
                                               self.gameState[4][5]))
        print("{0} {1} {2} {3} {4} {5} {6}".format(self.gameState[0][4],
                                                   self.gameState[1][4],
                                                   self.gameState[2][4],
                                                   self.gameState[3][4],
                                                   self.gameState[4][4],
                                                   self.gameState[5][4],
                                                   self.gameState[6][4]))
        print("{0} {1} {2} {3} {4} {5} {6}".format(self.gameState[0][3],
                                                   self.gameState[1][3],
                                                   self.gameState[2][3],
                                                   self.gameState[3][3],
                                                   self.gameState[4][3],
                                                   self.gameState[5][3],
                                                   self.gameState[6][3]))
        print("{0} {1} {2} {3} {4} {5} {6}".format(self.gameState[0][2],
                                                   self.gameState[1][2],
                                                   self.gameState[2][2],
                                                   self.gameState[3][2],
                                                   self.gameState[4][2],
                                                   self.gameState[5][2],
                                                   self.gameState[6][2]))
        print("      {0} {1} {2}      ".format(self.gameState[2][1],
                                               self.gameState[3][1],
                                               self.gameState[4][1]))
        print("      {0} {1} {2}      ".format(self.gameState[2][0],
                                               self.gameState[3][0],
                                               self.gameState[4][0]))

    def constructor(self):
        self.score = 0.0;
        self.leafP = False
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

        # for (int j=3;j<=7;j++)
        # {
        #     for (int i=1;i<=7;i++)
        #         {
        #             if (j==3 && i>=3 && i<=5)
        #                 continue;
        #             if (j>=6 && (i<3 || i>5))
        #                 continue;
        #             gameState[i-1][j-1] = 1;
        #         }
        # }

        # gameState[2][0]=2;
        # gameState[4][0]=2;

    def setP1(self, a_string):
        pass

    def setP2(self, a_string):
        pass

    def geeseWinP(self):
        pass

    def foxesWinP(self):
        pass
