# Using a function rand5() that returns an integer from 1 to 5 (inclusive)
# with uniform probability, implement a function rand7() that returns an integer
# from 1 to 7 (inclusive).

from random import randint

def rand5():
    return randint(1, 5)


def rand7():
    ans = 25
    while ans > 21:
        # 5 is the minimum number that flatten the random func.
        # ans \in [1, 25]
        ans = (rand5() - 1) * 5 + rand5()

    return ans % 7 + 1


def another():
    ans = 125
    while ans > 119:
        ans = (rand5() - 1) * 5 * 5 + (rand5() - 1) * 5 + rand5()

    return ans % 7 + 1


if __name__ == '__main__':
    count = [0] * 7
    for i in range(7000):
        rand = rand7()
        count[rand-1] += 1

    print(count)
