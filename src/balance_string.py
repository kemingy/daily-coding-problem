# You're given a string consisting solely of (, ), and *. * can represent
# either a (, ), or an empty string. Determine whether the parentheses are
# balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.


def is_balanced(string):
    if not string:
        return True

    low, high = 0, 0
    for s in string:
        low += 1 if s == "(" else -1
        high += 1 if s != ")" else -1
        if high < 0:
            return False

        low = max(low, 0)

    return low == 0


if __name__ == "__main__":
    for s in ["(()*", "(*)", ")*(", "*("]:
        print(s, is_balanced(s))
