# Given this matrix, a start coordinate, and an end coordinate, return the 
# minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. You can move up, left, down, 
# and right. You cannot move through walls. You cannot wrap around the edges of
# the board.


def min_step(maze, start, end):
    checked, candidates = set(), set([(start[0], start[1])])
    
    if len(maze) == 0 or len(maze[0]) == 0:
        return None

    row, col = len(maze), len(maze[0])

    if start == end:
        return 0

    def check_if_reachable(x, y):
        if x < 0 or x >= row:
            return False
        if y < 0 or y >= col:
            return False
        if (x, y) in checked or maze[x][y]:
            return False
        return True

    if not (check_if_reachable(start[0], start[1]) and check_if_reachable(end[0], end[1])):
        return None

    step = 0
    while candidates:
        next_candidates = set()
        for cand in candidates:
            checked.add((cand[0], cand[1]))
            for (r, c) in [
                (cand[0] + x, cand[1] + y) for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    if check_if_reachable(cand[0] + x, cand[1] + y)]:
                next_candidates.add((r, c))

        step += 1

        print(step, next_candidates)

        if (end[0], end[1]) in next_candidates:
            return step

        candidates = next_candidates


if __name__ == '__main__':
    maze = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False],
    ]
    print('Min step: {}'.format(min_step(maze, (3, 0), (0, 0))))
