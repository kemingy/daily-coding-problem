# Given an arithmetic expression in Reverse Polish Notation, write a program
# to evaluate it.

# The expression is given as a list of numbers and operands. For example:
# [5, 3, '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
# should return 5, since it is equivalent to
# ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.


def evaluate(expressions):
    nums = []
    for e in expressions:
        if isinstance(e, str):
            x = nums.pop()
            y = nums.pop()
            if e == "+":
                n = y + x
            elif e == "-":
                n = y - x
            elif e == "*":
                n = y * x
            elif e == "/":
                n = y / x
            else:
                print("Unknown operator: {}".format(e))
                break
            nums.append(n)
        else:
            nums.append(e)

    return nums[0]


if __name__ == "__main__":
    print(evaluate([15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"]))
