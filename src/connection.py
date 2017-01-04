""" Stores connection info between game nodes (positions) """

from src import helper

class Connection(object):
    """ Stores connection info between game nodes (positions) """

    def __init__(self):
        self.startX = None # int
        self.startY = None # int
        self.direction = None # int
        self.endX = None # int
        self.endY = None # int

    def setstartX(self, value):
        """ Setter for startX with type checking """
        helper.checkIfInt(value)
        self.startX = value

    def setstartY(self, value):
        """ Setter for startY with type checking """
        helper.checkIfInt(value)
        self.startY = value

    def setdirection(self, value):
        """ Setter for direction with type checking """
        helper.checkIfInt(value)
        self.direction = value

    def setendX(self, value):
        """ Setter for endX with type checking """
        helper.checkIfInt(value)
        self.endX = value

    def setendY(self, value):
        """ Setter for endY with type checking """
        helper.checkIfInt(value)
        self.endY = value
