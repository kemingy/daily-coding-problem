# Suppose you are given a table of currency exchange rates, represented as a 2D 
# array. Determine whether there is a possible arbitrage: that is, whether 
# there is some sequence of trades you can make, starting with some amount A of 
# any currency, so that you can end up with some amount greater than A of that 
# currency.

from math import log
from random import random
from copy import deepcopy

def find_arbitrage(table):
    graph = [[log(rate) for rate in row] for row in table]

    n = len(table)
    min_distance = [float('inf')] * n
    min_distance[0] = 0

    for _ in range(n - 1):
        for row in range(n):
            for col in range(n):
                if min_distance[col] > min_distance[row] + graph[row][col]:
                    min_distance[col] = min_distance[row] + graph[row][col]

    for row in range(n):
        for col in range(n):
            if min_distance[col] > min_distance[row] + graph[row][col]:
                return True

    return False


def floyd_arbitrage(rate):
    n = len(rate)
    dist = deepcopy(rate)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]

    print(dist)
    found = False
    for i in range(n):
        if dist[i][i] > 1:
            print('Case {} can be used in arbitrage.'.format(i))
            found = True

    return found


if __name__ == '__main__':
    n = 5
    for _ in range(1):
        rate = [[1 + (random() - 0.6) / 10 for i in range(n)] for j in range(n)]

        print('rate matrix:')
        for row in rate:
            print(row)

        if not floyd_arbitrage(rate):
            print('Impossible.')

        print('-' * 80)
