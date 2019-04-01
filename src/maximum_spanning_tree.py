# Recall that the minimum spanning tree is the subset of edges of a tree that
# connect all its vertices with the smallest possible total edge weight.

# Given an undirected graph with weighted edges, compute the maximum weight
# spanning tree.

from random import randint

def max_spanning_tree(weights):
    nodes = set()
    path = []
    for (x, y) in sorted(weights.keys(), key=lambda x: weights.get(x), reverse=True):
        if len(nodes) >= 10:
            break
        if x not in nodes or y not in nodes:
            path.append((x, y, weights.get((x, y))))
            nodes.add(x)
            nodes.add(y)

    return path

if __name__ == '__main__':
    weights = {}
    n = 10
    for i in range(n):
        for j in range(i + 1, n):
            weights[(i, j)] = randint(1, 100)

    print(max_spanning_tree(weights))