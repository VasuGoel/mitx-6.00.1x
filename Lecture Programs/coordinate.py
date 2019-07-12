class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordinate_object):
        x_diff_sq = (self.x - other_coordinate_object.x)**2
        y_diff_sq = (self.y - other_coordinate_object.y)**2
        return (x_diff_sq + y_diff_sq)**0.5



# Origin
o = Coordinate(0, 0)
# Point
p = Coordinate(6, 9)


print(f'The distance between point o({o.x},{o.y}) and p({p.x},{p.y}) is: {round(o.distance(p), 2)} units')
