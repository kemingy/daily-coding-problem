# At a popular bar, each customer has a set of favorite drinks, and will
# happily accept any drink among this set. For example, in the following
# situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

# preferences = {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }

# A lazy bartender working at this bar is trying to reduce his effort by
# limiting the drink recipes he must memorize. Given a dictionary input such
# as the one above, return the fewest number of drinks he must learn in
# order to satisfy all customers.

# For the input above, the answer would be 2, as drinks 1 and 5 will
# satisfy everyone.


def fewest_drink(pref):
    drink2person = {}
    for person, drinks in pref.items():
        for drink in drinks:
            if drink not in drink2person:
                drink2person[drink] = set()
            drink2person[drink].add(person)

    ans = []
    satisfied = set()
    people = len(pref)
    while len(satisfied) != people:
        most_favorite = sorted(
            drink2person.keys(),
            key=lambda key: len(drink2person[key] - satisfied),
            reverse=True)
        drink = most_favorite[0]
        ans.append(drink)
        satisfied |= drink2person[drink]
        del drink2person[drink]

    return ans


if __name__ == "__main__":
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }
    print(fewest_drink(preferences))
