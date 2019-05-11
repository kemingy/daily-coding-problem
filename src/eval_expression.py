# Given a string consisting of parentheses, single digits, and positive and
# negative signs, convert the string into a mathematical expression to obtain
# the answer.

# Don't use eval or a similar built-in parser.

# For example, given '-1 + (2 + 3)', you should return 4.


def add(x, y): return x + y


def sub(x, y): return x - y


def eval_expr(expr, index=0):
    digits = []
    operator = None
    while index < len(expr):
        if expr[index] == ' ':
            pass
        elif expr[index] == '(':
            digits.append(eval_expr(expr, index=index+1))
            index = expr.find(')', index)
        elif expr[index] == ')':
            return digits[0] if digits else 0
        elif expr[index] == '+':
            if not digits:
                digits.append(0)
            operator = add
        elif expr[index] == '-':
            if not digits:
                digits.append(0)
            operator = sub
        elif 48 <= ord(expr[index]) <= 57:
            digits.append(ord(expr[index]) - 48)
        else:
            raise ValueError('Unknown character: {}'.format(expr[index]))

        if len(digits) == 2:
            digits = [operator(*digits)]
            operator = None

        index += 1

    return digits[0] if digits else 0


if __name__ == "__main__":
    print(eval_expr('-1 + (2 + 3)'))
