import cProfile

import time

from res import types
from src import ai
from src import coordinate
from src import historynode

plyNum = 5
aiObject = ai.AI()
game = historynode.HistoryNode()

game.setState(coordinate.Coordinate(3, 7), types.GOOSE)
game.setState(coordinate.Coordinate(4, 7), types.GOOSE)
game.setState(coordinate.Coordinate(5, 7), types.GOOSE)

game.setState(coordinate.Coordinate(4, 6), types.GOOSE)
game.setState(coordinate.Coordinate(5, 6), types.GOOSE)

game.setState(coordinate.Coordinate(1, 5), types.GOOSE)
game.setState(coordinate.Coordinate(4, 5), types.GOOSE)
game.setState(coordinate.Coordinate(5, 5), types.GOOSE)
game.setState(coordinate.Coordinate(6, 5), types.FOX)
game.setState(coordinate.Coordinate(7, 5), types.GOOSE)

game.setState(coordinate.Coordinate(1, 4), types.GOOSE)
game.setState(coordinate.Coordinate(2, 4), types.FOX)
game.setState(coordinate.Coordinate(7, 4), types.GOOSE)

game.setState(coordinate.Coordinate(1, 3), types.GOOSE)
game.setState(coordinate.Coordinate(2, 3), types.GOOSE)
game.setState(coordinate.Coordinate(3, 3), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(4, 3), types.SUPERGOOSE)

game.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
game.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)

game.pretty_print_board()

start = time.time()
actualValue = aiObject.iterativeDeepeningSearch(game, False, plyNum)
end = time.time()
print("Running again with cProfile")
aiObject2 = ai.AI()
cProfile.run('aiObject2.findBestMove(game, False, plyNum)')

actualValue.pretty_print_board()
print(actualValue.score)
print("New: Calculated {0} positions in {1:.3f} seconds at {2:.3f} pos/sec".format(
      aiObject.moveCount,
      end - start,
      aiObject.moveCount/(end-start)))
