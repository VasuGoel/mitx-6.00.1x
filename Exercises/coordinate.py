class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    # returns True if coordinates refer to same point in the plan
    def __eq__(self, other):
        # check to see if 'other' is same type
        assert type(other) == type(self)
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        return False

    # returns a string that looks like a valid Python expression that could be used to recreate an object with the same value.
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


# o = Coordinate(0, 0)
# p = Coordinate(9, 9)
# print(o == p)
# print(o.__repr__())
