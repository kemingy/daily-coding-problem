# You are given a starting state start, a list of transition probabilities for
# a Markov chain, and a number of steps num_steps. Run the Markov chain starting
# from start for num_steps and compute the number of times we visited each state.

# For example, given the starting state a, number of steps 5000, and the
# following transition probabilities:
# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]
# One instance of running this Markov chain might produce
# { 'a': 3012, 'b': 1656, 'c': 332 }.

from random import random


def simulate_markov(transition, steps=5000, start='a'):
    count = dict((key, 0) for key in transition)
    state = start
    for _ in range(steps):
        # find next state
        n = random()
        for s in transition[state]:
            n -= transition[state][s]
            if n <= 0:
                state = s
                count[state] += 1
                break

    return count


if __name__ == "__main__":
    print(
        simulate_markov(
            {
                'a': {
                    'a': 0.9,
                    'b': 0.075,
                    'c': 0.025,
                },
                'b': {
                    'a': 0.15,
                    'b': 0.8,
                    'c': 0.05,
                },
                'c': {
                    'a': 0.25,
                    'b': 0.25,
                    'c': 0.5,
                }
            }
        )
    )
