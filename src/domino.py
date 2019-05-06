# You are given an string representing the initial conditions of some dominoes.
# Each element can take one of three values:

# •	L, meaning the domino has just been pushed to the left,
# •	R, meaning the domino has just been pushed to the right, or
# •	., meaning the domino is standing still.

# Determine the orientation of each tile when the dominoes stop falling.

# Note that if a domino receives a force from the left and right side
# simultaneously, it will remain upright.

# For example, given the string .L.R....L, you should return LL.RRRLLL.
# Given the string ..R...L.L, you should return ..RR.LLLL.


from collections import namedtuple


Direction = namedtuple('Direction', ['index', 'dir'])

def domino(directions):
    n = len(directions)
    result = list(directions)
    dominoes = [Direction(i, d) for i, d in enumerate(directions) if d != '.']
    dominoes = [Direction(-1, 'L')] + dominoes + [Direction(n, 'R')]

    for i in range(len(dominoes)-1):
        j = i + 1
        if dominoes[i].dir == dominoes[j].dir:
            for k in range(dominoes[i].index+1, dominoes[j].index):
                result[k] = dominoes[i].dir
        elif dominoes[i].dir > dominoes[j].dir: # R > L
            for k in range(dominoes[i].index+1, dominoes[j].index):
                x, y = k - dominoes[i].index, dominoes[j].index - k
                result[k] = '.LR'[(x > y) - (x < y)]

    return ''.join(result)



if __name__ == "__main__":
    for dir in ['.L.R....L', '..R...L.L', '.L.R...LR..L..']:
        print(dir, '->', domino(dir))