# A builder is looking to build a row of N houses that can be of K different 
# colors. He has a goal of minimizing cost while ensuring that no two 
# neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to 
# build the nth house with kth color, return the minimum cost which achieves 
# this goal.


def min_cost(cost):
    if len(cost) == 0 or len(cost[0]) == 0:
        return 0

    def helper_func(row, forbidden):
        if row >= len(cost):
            return 0

        return min([n + helper_func(row + 1, i) for i, n in enumerate(cost[row]) if i != forbidden])

    return min([i + helper_func(1, i) for i in cost[0]])


if __name__ == '__main__':
    cost = [
        [2, 3, 4, 1, 2],
        [3, 6, 1, 5, 4],
        [8, 7, 1, 9, 5],
        [4, 1, 2, 3, 4],
    ]
    print(min_cost(cost))
