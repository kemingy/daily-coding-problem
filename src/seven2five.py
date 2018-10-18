# Using a function rand7() that returns an integer from 1 to 7 (inclusive) 
# with uniform probability, implement a function rand5() that returns an 
# integer from 1 to 5 (inclusive).


from random import randint

def rand7():
    return randint(1, 7)


def rand5():
    ans = rand7()
    while ans > 5:
        ans = rand7()

    return ans


if __name__ == '__main__':
    count = [0] * 5
    for _ in range(5000):
        count[rand5() - 1] += 1

    print(count)
