class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
    
    # method overloading
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return f'Your second argument must be a Point.'
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return f'Your second argument must be a Point.'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other, self.z * other)
        else:
            return f'Your second argument must be an integer.'

    def __div__(self, other):
        if isinstance(other, int):
            return Point(self.x / other, self.y / other, self.z / other)
        else:
            return f'Your second argument must be an integer.'


p1 = Point(1, 2, 3)
p2 = Point(1,2,3)
print(p1 * 3)
