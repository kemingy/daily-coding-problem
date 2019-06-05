# A group of houses is connected to the main water plant by means of a set of
# pipes. A house can either be connected by a set of pipes extending directly
# to the plant, or indirectly by a pipe to a nearby house which is otherwise
# connected.

# For example, here is a possible configuration, where A, B, and C are houses,
# and arrows represent pipes:

# A <--> B <--> C <--> plant

# Each pipe has an associated cost, which the utility company would like to
# minimize. Given an undirected graph of pipe connections, return the lowest
# cost configuration of pipes such that each house has access to water.

# In the following setup, for example, we can remove all but the pipes from
# plant to A, plant to B, and B to C, for a total cost of 16.

# pipes = {
#     'plant': {'A': 1, 'B': 5, 'C': 20},
#     'A': {'C': 15},
#     'B': {'C': 10},
#     'C': {}
# }


def lowest_cost(pipes):
    cost = {key: float('inf') for key in pipes if key != 'plant'}
    cost['plant'] = 0
    changed = True
    while changed:
        changed = False
        for node, neighbers in pipes.items():
            for n in neighbers:
                if cost[node] + neighbers[n] < cost[n]:
                    cost[n] = cost[node] + neighbers[n]
                    changed = True
                    break

    del cost['plant']
    return cost


if __name__ == "__main__":
    for pipes in [
        {
            'plant': {'A': 1, 'B': 5, 'C': 20},
            'A': {'C': 15},
            'B': {'C': 10},
            'C': {}
        },
        {
            'plant': {'C': 20, 'B': 10},
            'A': {'C': 5},
            'B': {'A': 2},
            'C': {}
        }
    ]:
        print(lowest_cost(pipes))
