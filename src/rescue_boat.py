# An imminent hurricane threatens the coastal town of Codeville. If at most two
# people can fit in a rescue boat, and the maximum weight limit for a given
# boat is k, determine how many boats will be needed to save everyone.

# For example, given a population with weights [100, 200, 150, 80] and a boat
# limit of 200, the smallest number of boats required will be three.


def boat_needed(weights):
    weights.sort()
    i, j = 0, len(weights) - 1
    count = 0
    while i < j:
        if weights[i] + weights[j] > 200:
            count += 1
            j -= 1
        elif weights[i] + weights[j] <= 200:
            count += 1
            i += 1
            j -= 1
    if i == j:
        count += 1
    return count


if __name__ == "__main__":
    for weights in [[100, 200, 150, 80], [180, 75, 120, 130, 100]]:
        print(weights, boat_needed(weights))
