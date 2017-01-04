""" Helper functions shared between 2 or more modules"""

def checkIfInt(value):
    """ Type checker for values to determine if they are of type int """
    if not isinstance(value, int):
        raise TypeError(("value is not an int. "
                         "value = {0}").format(value))