from src import helper

class Coordinate(object):
    """ Simple interface to pass game coordinates around """
    """ Can return 2 types of coordinates: """
    """ Board - The coordinate on a board, which is 1-indexed """
    """     and is used in the constructor. """
    """ Array - Coordinate in the array, which is 0-indexed """
    def __init__(self, x, y):
        helper.checkIfInt(x)
        helper.checkIfInt(y)
        helper.checkIfCoordinateIsValid(x, y)
        self.x = x
        self.y = y

    def get_x_board(self):
        return self.x

    def get_y_board(self):
        return self.y

    def get_x_array(self):
        return self.x - 1

    def get_y_array(self):
        return self.y - 1