# You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN)
# representing a polygon. You can assume these points are given in order;
# that is, you can construct the polygon by connecting point 1 to point 2,
# point 2 to point 3, and so on, finally looping around to connect point N
# to point 1.

# Determine if a new point p lies inside this polygon. (If p is on the boundary
# of the polygon, you should return False).


from enum import Enum


class Segment(Enum):
    Colinear = 0
    Clockwise = 1
    CounterClockwise = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point::<({}, {})>'.format(self.x, self.y)


def orientation(a, b, c):
    ans = (b.y - a.y) * (c.x - a.x) - (c.y - a.y) * (b.x - a.x)
    if ans == 0:
        return Segment.Colinear
    return Segment.Clockwise if ans > 0 else Segment.CounterClockwise


def on_segment(a, b, c):
    if min(a.x, c.x) <= b.x <= max(a.x, c.x) and min(a.y, c.y) <= b.y <= max(a.y, c.y):
        return True
    return False


def intersect(a, b, c, d):
    orders = [(a, c, b), (a, d, b), (c, a, d), (c, b, d)]
    orientations = []
    for i, order in enumerate(orders):
        orientations.append(orientation(*order))
        if on_segment(*order) and orientations[i] == Segment.Colinear:
            return True
    if orientations[0] != orientations[1] and orientations[2] != orientations[3]:
        return True
    return False


class Polygon:
    def __init__(self, points):
        self.points = points
        self.n = len(points)

    def contain(self, point):
        ext = Point(float('inf'), point.y)
        count = 0
        for i in range(self.n):
            if intersect(self.points[i], self.points[(i+1) % self.n], point, ext):
                if orientation(self.points[i], self.points[(i+1) % self.n], point) == Segment.Colinear:
                    if on_segment(self.points[i], point, self.points[(i+1) % self.n]):
                        return False
                count += 1
        return True if count & 1 else False


if __name__ == '__main__':
    polygon = Polygon([
        Point(0, 0), Point(1, 8), Point(3, 20), Point(10, 12), Point(15, 2)
    ])
    for p in [Point(0, 2), Point(12, 15), Point(14, 4), Point(4, 5)]:
        print('Is {} in Polygon? {}'.format(p, polygon.contain(p)))
