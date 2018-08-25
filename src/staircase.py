# Given N, write a function that returns the number of unique ways you can climb
# the staircase.

STEPS = [1, 3, 5]

def climb_staircase(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    return sum([climb_staircase(n - i) for i in STEPS])


if __name__ == '__main__':
    for step in range(2, 10):
        print('Step: {}, unique ways: {}'.format(step, climb_staircase(step)))
