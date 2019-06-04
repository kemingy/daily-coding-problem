# A girl is walking along an apple orchard with a bag in each hand. She likes
# to pick apples from each tree as she goes along, but is meticulous about not
# putting different kinds of apples in the same bag.

# Given an input describing the types of apples she will pass on her path,
# in order, determine the length of the longest portion of her path that
# consists of just two types of apple trees.

# For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion
# will involve types 1 and 3, with a length of four.


def longest_portion(types):
    x, y = 0, None
    length = 1
    longest = 0

    for i in range(1, len(types)):
        if types[i] == types[x]:
            length += 1
        elif y is None:
            y = i
            length += 1
        elif types[i] == types[y]:
            length += 1
        else:
            if length > longest:
                longest = length

            for j in range(i-1, -1, -1):
                if types[j] != types[i-1]:
                    break
                x = j

            y = i
            length = i - x + 1

    return longest


if __name__ == "__main__":
    for types in [[2, 1, 2, 3, 3, 1, 3, 5], [1, 4, 2, 2, 4, 1, 2, 1]]:
        print(types, longest_portion(types))
