""" This module contains the AI search algorithm """

from src import coordinate
from src import historynode

# This function takes a game state and returns a score for the position.
# A positive score favors the geese, and a negative score favors the foxes.
def evaluationFunction(theGame):
    valueA = 0.0
    valueB = 0.0
    victoryPoints = 0
    totalScore = 0.0
    return totalScore

# -(float) evaluationFunction: (HistoryNode *) theGame;
#     float valueA = 0.0;
#     float valueB = 0.0;
#     float victoryPoints = 0;
#     float totalScore = 0.0;

#     #calculates value A: material considerations
#     for (int i=0;i<7;i++)
#         for (int j=0;j<7;j++)
#             if ([theGame getState:i :j]<1)
#                 continue;
#             else if ([theGame getState:i :j]==1)
#                 valueA+=1;
#             else if ([theGame getState:i :j]==3)
#                 valueA+=2;
#                 #value B: calculates closeness to victory
#                 if (i>=2 && i<=4 && j>=0 && j<=2)
#                     valueB+=3-j;
#                     victoryPoints+=1;

#     valueA-=20;
#     valueB *= victoryPoints; 
#     totalScore += weightA*valueA + weightB*valueB;
#     evaluated+=1;
#     #checks if geese win
#     if ([theGame geeseWinP])
#         totalScore+=1000.0;
#     #checks if foxes win
#     else if ([theGame foxesWinP])
#         totalScore-=1000.0;
#     return totalScore;

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
