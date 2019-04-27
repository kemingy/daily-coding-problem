# The transitive closure of a graph is a measure of which vertices are reachable
# from other vertices. It can be represented as a matrix M, where M[i][j] == 1
# if there is a path between vertices i and j, and otherwise 0.

# For example, suppose we are given the following graph in adjacency list form:
# graph = [
#     [0, 1, 3],
#     [1, 2],
#     [2],
#     [3]
# ]
# The transitive closure of this graph would be:
# [1, 1, 1, 1]
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
# Given a graph, find its transitive closure.


def closure(graph):
    n = len(graph)
    matrix = [[0 for _ in range(n)] for row in range(n)]
    for i in range(n):
        for j in graph[i]:
            matrix[i][j] = 1

    for i in range(n-2, -1, -1):
        path = [p for p in range(i+1, n) if matrix[i][p] == 1]
        if not path:
            continue
        for j in range(i-1, -1, -1):
            if matrix[j][i] == 1:
                for p in path:
                    matrix[j][p] = 1

    return matrix


if __name__ == '__main__':
    graph = [
        [0, 1, 3],
        [1, 2],
        [2,],
        [3,],
    ]
    print(closure(graph))