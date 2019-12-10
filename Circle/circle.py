import math


class Circle:
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius**2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @area.setter
    def area(self, area):
        raise AttributeError(f'Cannot set attribute Area')

    def __repr__(self):
        return f'Circle({self.radius})'



c = Circle(-1.5)
print(c.area)
c.radius = 3
print(c.area)
c.diameter = 3
print(c.area)
c.radius = -1
print(c.area)