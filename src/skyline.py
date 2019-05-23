# The skyline of a city is composed of several buildings of various widths
# and heights, possibly overlapping one another when viewed from a distance.
# We can represent the buildings using an array of (left, right, height) tuples,
# which tell us where on an imaginary x-axis a building begins and ends, and
# how tall it is. The skyline itself can be described by a list of (x, height)
# tuples, giving the locations at which the height visible to a distant observer
# changes, and each new height.

# Given an array of buildings as described above, create a function that
# returns the skyline.

# For example, suppose the input consists of the buildings
# [(0, 15, 3), (4, 11, 5), (19, 23, 4)].

# In aggregate, these buildings would create a skyline that looks like the
# one below.

#      ______
#     |      |        ___
#  ___|      |___    |   |
# |   |   B  |   |   | C |
# | A |      | A |   |   |
# |   |      |   |   |   |
# ------------------------

# As a result, your function should return
# [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].

from collections import namedtuple

Point = namedtuple('Point', ['index', 'height', 'is_left'])

def skyline(buildings):
    points = []
    for building in buildings:
        points.append(Point(building[0], building[2], True))
        points.append(Point(building[1], building[2], False))

    points.sort(key=lambda p: p.index)
    last = points[0]
    n = len(points)
    ans = [(last.index, last.height)]
    for i in range(1, len(points)):
        p = points[i]
        if p.is_left:
            ans.append((p.index, p.height))
        elif i != n-1 and not points[i+1].is_left:
            ans.append((p.index, points[i+1].height))
        else:
            ans.append((p.index, 0))

    return ans


if __name__ == "__main__":
    print(skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]))
