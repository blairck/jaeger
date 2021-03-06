""" Helper functions shared between 2 or more modules"""

def checkIfCoordinateIsValid(x, y):
    """ Check if board values constitute a valid location on the board """
    if x < 1 or x > 7:
        raise ValueError("Invalid board coordinate value, X: ({0}, {1})"
                         .format(x, y))
    if y < 1 or y > 7:
        raise ValueError("Invalid board coordinate value, Y: ({0}, {1})"
                         .format(x, y))
    if x in (1, 2, 6, 7):
        if y in (1, 2, 6, 7):
            raise ValueError("Invalid board coordinate values: ({0}, {1})"
                             .format(x, y))
