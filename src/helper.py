""" Helper functions shared between 2 or more modules"""

def checkIfInt(value):
    """ Type checker for values to determine if they are of type int """
    if not isinstance(value, int):
        raise TypeError(("value is not an int. "
                         "value = {0}").format(value))

def checkIfCoordinateIsValid(coordinate):
    """ Check if a coordinate value is a valid location on the board """
    x = coordinate.get_x_board()
    y = coordinate.get_y_board()
    if x < 1 or x > 7:
        raise ValueError("Invalid board coordinate value, X: ({0}, {1})"
                         .format(x, y))
    if y < 1 or y > 7:
        raise ValueError("Invalid board coordinate value, Y: ({0}, {1})"
                         .format(x, y))
    if coordinate.get_x_board() in (1, 2, 6, 7):
        if coordinate.get_y_board() in (1, 2, 6, 7):
            raise ValueError("Invalid board coordinate values: ({0}, {1})"
                             .format(x, y))
