class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordinate_object):
        x_diff_sq = (self.x - other_coordinate_object.x)**2
        y_diff_sq = (self.y - other_coordinate_object.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    # Python calls __str__ method when used with 'print' on your class object
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Override the operators to work with objects
    def __add__(self, other_coordinate_object):
        return f'({self.x + other_coordinate_object.x}, {self.y + other_coordinate_object.y})'




# Origin
o = Coordinate(0, 0)
# Point
p = Coordinate(6, 9)

print(f'The distance between point o({o.x},{o.y}) and p({p.x},{p.y}) is: {round(o.distance(p), 2)} units')
print(f'Distance - {Coordinate.distance(o, p)}')

# print(p) returns <__main__.Coordinate object at 0x109c699e8> which is 'uninformative'. We define a '__str__' method in class to define what we wanna do with that print(c)
print(p)

print(f'Addition of point o({o.x},{o.y}) and p({p.x},{p.y}) is: {Coordinate.__add__(o, p)}')
