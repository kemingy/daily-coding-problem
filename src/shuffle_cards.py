# Given a function that generates perfectly random numbers between 1 and k 
# (inclusive), where k is an input, write a function that shuffles a deck of 
# cards represented as an array using only swaps.

from random import randint

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def rand_k(k, limit):
    power = 1
    while k < limit:
        k *= k
        power += 1

    multiple = limit * (k ** power // limit)
    ans = multiple
    while ans >= multiple:
        ans = randint(1, k)
        for _ in range(power - 1):
            ans += k * (randint(1, k) - 1)

    return ans % limit

def shuffle(array, k):
    for i in range(52):
        j = i + rand_k(k, 52 - i)
        swap(array, i, j)


if __name__ == '__main__':
    count = [0] * 52
    for k in range(12, 2222):
        deck = list(range(1, 53))
        shuffle(deck, k)
        count = [count[i] + deck[i] for i in range(52)]

    print(count)