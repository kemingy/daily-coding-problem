# In a directed graph, each node is assigned an uppercase letter. We define a 
# path's value as the number of most frequently-occurring letter along that path.
# For example, if a path in the graph goes through "ABACA", the value of the 
# path is 3, since there are 3 occurrences of 'A' on the path.
# Given a graph with n nodes and m directed edges, return the largest value 
# path of the graph. If the largest value is infinite, then return null.

from collections import Counter

def path_value(nodes, edges):
    paths = []
    unique = []
    for e in edges:
        linked = False
        for i, p in enumerate(paths):
            if p and p[-1][1] == e[0]:
                p.append(e)
                if e[1] not in unique[i]:
                    unique[i].add(e[1])
                else:
                    return None
                linked = True

        if not linked:
            if e[0] == e[1]:
                return None
            paths.append([e])
            unique.append(set(e))

    # print(paths, unique)
    value = 0
    for u in unique:
        c = Counter([nodes[i] for i in u])
        value = max(value, c.most_common(1)[0][1])

    return value


if __name__ == '__main__':
    for nodes, edges in [
        ('ABACA', [(0, 1), (0, 2), (2, 3), (3, 4)]),
        ('A', [(0, 0)]),
    ]:
        print('Path value of {} is {}.'.format(edges, path_value(nodes, edges)))
