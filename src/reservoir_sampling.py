# Given a stream of elements too large to store in memory, pick a random element
# from the stream with uniform probability.

import random

def reservoir_sampling(stream):
    ans = None

    for i, e in enumerate(stream):
        if i == 0:
            ans = e
        elif random.randint(1, i + 1) == 1:
            ans = e

    return ans
