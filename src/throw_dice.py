# Write a function, throw_dice(N, faces, total), that determines how many ways
# it is possible to throw N dice with some number of faces each to get a
# specific total.

# For example, throw_dice(3, 6, 7) should equal 15.


def throw_dice(n, faces, total):
    if n < 1 or n > total or n * faces < total:
        return 0
    elif n == 1 and faces >= total:
        return 1
    return sum([throw_dice(n-1, faces, total-f) for f in range(1, faces+1)])


if __name__ == "__main__":
    print(throw_dice(3, 6, 7))
