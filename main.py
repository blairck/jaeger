from res import types
from src import ai
from src import coordinate
from src import historynode
from src import interface

if __name__ == '__main__':
    """
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

    game.setState(coordinate.Coordinate(3, 1), types.FOX)
    game.setState(coordinate.Coordinate(5, 1), types.FOX)

    while(True):
        game.pretty_print_board()
        aiObject = ai.AI(0.5, 0.5)
        computerGooseP = False
        game = aiObject.findBestMove(game, computerGooseP, 3)

        print("----------------------------")
        game.pretty_print_board()
        legalMoves = aiObject.getAllMovesForPlayer(game, not computerGooseP)
        while(True):
            userInput = input('Enter a move: ')
            result = interface.getPositionFromListOfMoves(legalMoves,
                                                          str(userInput),
                                                          not computerGooseP)
            if len(result) != 1:
                print("Unknown or invalid move, please try again")
                continue
            else:
                game = result[0]
                break
