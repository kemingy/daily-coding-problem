# In chess, the Elo rating system is used to calculate player strengths based
# on game results.

# A simplified description of the Elo system is as follows. Every player begins
# at the same score. For each subsequent game, the loser transfers some points
# to the winner, where the amount of points transferred depends on how unlikely
# the win is. For example, a 1200-ranked player should gain much more points
# for beating a 2000-ranked player than for beating a 1300-ranked player.

# Implement this system.


def logistic_expectation(rx, ry):
    return 1 / (1 + 10 ** ((ry - rx) / 400))


def update_score(rx, ry, k=16):
    return rx + k * (1 - logistic_expectation(rx, ry))


if __name__ == '__main__':
    print('1200-rank win 2000-rank: {}'.format(update_score(1200, 2000)))
    print('1200-rank win 1300-rank: {}'.format(update_score(1200, 1300)))
