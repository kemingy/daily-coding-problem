# A classroom consists of N students, whose friendships can be represented in
# an adjacency list. For example, the following descibes a situation where 0
# is friends with 1 and 2, 3 is friends with 6, and so on.

# {0: [1, 2],
#  1: [0, 5],
#  2: [0],
#  3: [6],
#  4: [],
#  5: [1],
#  6: [3]}

# Each student can be placed in a friend group, which can be defined as the
# transitive closure of that student's friendship relations. In other words,
# this is the smallest set such that no student in the group has any friends
# outside this group. For the example above, the friend groups would be
# {0, 1, 2, 5}, {3, 6}, {4}.

# Given a friendship list such as the one above, determine the number of
# friend groups in the class.


def friend_group(adjacency):
    groups = []
    mapping = {}
    for i in adjacency:
        if i in mapping:
            continue
        for adj in adjacency[i]:
            if adj in mapping:
                groups[mapping[adj]].add(i)
                mapping[i] = mapping[adj]
        if i not in mapping:
            mapping[i] = len(groups)
            groups.append({i})

    return groups


if __name__ == '__main__':
    print(friend_group({
        0: [1, 2],
        1: [0, 5],
        2: [0],
        3: [6],
        4: [],
        5: [1],
        6: [3]
    }))
