# Given an undirected graph represented as an adjacency matrix and an integer k,
# write a function to determine whether each vertex in the graph can be colored
# such that no two adjacent vertices share the same color using at most k colors.

def color_adj_matrix(adj, k):
    assert len(adj) == len(adj[0])

    n = len(adj)
    color = [-1] * n

    color[0] = 0
    for i in range(1, n):
        adj_color = set()
        for j in range(n):
            if i != j and adj[i][j] == 1:
                adj_color.add(color[j])

        min_color = min([c for c in range(n) if c not in adj_color])
        color[i] = min_color

    print('color of node: {}'.format(color))
    return max(color) >= k


if __name__ == '__main__':
    adj = [
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1],
    ]
    print(color_adj_matrix(adj, 3))
