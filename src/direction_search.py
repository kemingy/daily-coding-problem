# You are in an infinite 2D grid where you can move in any of the 8 directions:
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover 
# the points. Give the minimum number of steps in which you can achieve it.
# You start from the first point.

def min_step(points):
    step = 0
    for i in range(1, len(points)):
        x = abs(points[i][0] - points[i - 1][0])
        y = abs(points[i][1] - points[i - 1][1])
        step += max(x, y)

    return step


if __name__ == '__main__':
    for points in [
        [(4, 2), (3, 1), (7, 8)],
        [(0, 0), (1, 1), (1, 2)],
    ]:
        print(points, end=': ')
        print(min_step(points))