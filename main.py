from random import shuffle

from res import types
from src import ai
from src import coordinate
from src import historynode
from src import interface

from settings import (DISPLAYEVALUATION,
                      SEARCHPLY,
                      STANDARD,
                      USERPLAYSFOX)

def aPlayerHasWon(game):
    """ Check game state to see if a player has won """
    if game.geeseWinP():
        print("Geese win!")
        return True
    elif game.foxesWinP():
        print("Foxes win!")
        return True
    return False

def determineDraw(game, ai):
    """ Check game state to see if it is drawn """
    if ai.evaluationFunction(game, True) is None:
        print("Game is a draw")
        return True
    return False

def setTwoRandomFoxCoordinatesInVictoryArea(game):
    """ Randomize the fox starting positions """
    possibleCoordinates = []
    for x in range(3, 6):
        for y in range(1, 4):
            possibleCoordinates.append(coordinate.Coordinate(x, y))
    shuffle(possibleCoordinates)
    game.setState(possibleCoordinates.pop(), types.FOX)
    game.setState(possibleCoordinates.pop(), types.FOX)

def createStartingPosition(standard):
    """
    Generates the starting position board. Can optionally randomize fox
    positions if standard is true.
    7         G - G - G
              | \ | / |
    6         G - G - G
              | / | \ |
    5 G - G - G - G - G - G - G
      | \ | / | \ | / | \ | / |
    4 G - G - G - G - G - G - G
      | / | \ | / | \ | / | \ |
    3 G - G - . - . - . - G - G
              | \ | / |
    2         . - . - .
              | / | \ |
    1         F - . - F
      1   2   3   4   5   6   7
    """
    game = historynode.HistoryNode()

    game.setState(coordinate.Coordinate(3, 7), types.GOOSE)
    game.setState(coordinate.Coordinate(4, 7), types.GOOSE)
    game.setState(coordinate.Coordinate(5, 7), types.GOOSE)

    game.setState(coordinate.Coordinate(3, 6), types.GOOSE)
    game.setState(coordinate.Coordinate(4, 6), types.GOOSE)
    game.setState(coordinate.Coordinate(5, 6), types.GOOSE)

    game.setState(coordinate.Coordinate(1, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(2, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(3, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(4, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(5, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(6, 5), types.GOOSE)
    game.setState(coordinate.Coordinate(7, 5), types.GOOSE)

    game.setState(coordinate.Coordinate(1, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(2, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(3, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(4, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(5, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(6, 4), types.GOOSE)
    game.setState(coordinate.Coordinate(7, 4), types.GOOSE)

    game.setState(coordinate.Coordinate(1, 3), types.GOOSE)
    game.setState(coordinate.Coordinate(2, 3), types.GOOSE)

    game.setState(coordinate.Coordinate(6, 3), types.GOOSE)
    game.setState(coordinate.Coordinate(7, 3), types.GOOSE)

    if standard:
        game.setState(coordinate.Coordinate(3, 1), types.FOX)
        game.setState(coordinate.Coordinate(5, 1), types.FOX)
    else:
        setTwoRandomFoxCoordinatesInVictoryArea(game)

    return game

if __name__ == '__main__':
    """ Main game loop. Play alternates between user and computer. """
    game = createStartingPosition(STANDARD)
    firstTurn = True

    aiObject = ai.AI()
    if USERPLAYSFOX:
        computersTurn = True
    else:
        computersTurn = False

    while(True):
        if not firstTurn:
            game.pretty_print_board()
            print("----------------------------")
        elif firstTurn and USERPLAYSFOX:
            game.pretty_print_board()
            print("----------------------------")

        if aPlayerHasWon(game):
            break
        elif determineDraw(game, aiObject):
            break

        if computersTurn:
            game = aiObject.iterativeDeepeningSearch(game,
                                                     USERPLAYSFOX,
                                                     SEARCHPLY)
            computersTurn = False

        game.pretty_print_board()
        if aPlayerHasWon(game):
            break
        elif determineDraw(game, aiObject):
            break

        if not game.score:
            game.score = aiObject.evaluationFunction(game)

        if DISPLAYEVALUATION:
            print("Score: {0:.2f}".format(game.score))

        legalMoves = aiObject.getAllMovesForPlayer(game,
                                                   not USERPLAYSFOX)
        while(True):
            userInput = input('Enter a move: ')
            result = interface.getPositionFromListOfMoves(game,
                                                          legalMoves,
                                                          str(userInput),
                                                          not USERPLAYSFOX)
            if len(result) != 1:
                print("Unknown or invalid move, please try again")
                continue
            else:
                game = result[0]
                computersTurn = True
                break

        firstTurn = False
