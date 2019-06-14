# You are presented with an array representing a Boolean expression.
# The elements are of two kinds:

# •	T and F, representing the values True and False.
# •	&, |, and ^, representing the bitwise operators for AND, OR, and XOR.

# Determine the number of ways to group the array elements using parentheses
# so that the entire expression evaluates to True.

# For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case,
# there are two acceptable groupings: (F | T) & T and F | (T & T).


def compute(x, op, y):
    if op == '&':
        return 'T' if x == 'T' and y == 'T' else 'F'
    elif op == '|':
        return 'T' if x == 'T' or y == 'T' else 'F'
    elif op == '^':
        return 'T' if x != y else 'F'


def num_of_true(values):
    results = []

    def helper(values, history):
        if len(values) == 1 and values[0] == 'T':
            results.append(history)
            return
        for i in range(len(values) - 2):
            new_value = values[:i] + [compute(*values[i:i+3])] + values[i+3:]
            new_history = history[:i] + \
                ['(' + ' '.join(history[i:i+3]) + ')'] + history[i+3:]
            helper(new_value, new_history)

    helper(values, values)
    return results


if __name__ == '__main__':
    for values in [['F', '|', 'T', '&', 'T'],
                   ['T', '^', 'F', '&', 'T', '|', 'F']]:
        print(num_of_true(values))
