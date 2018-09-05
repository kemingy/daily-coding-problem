# Given a string of round, curly, and square open and closing brackets, return 
# whether the brackets are balanced (well-formed).

def is_balance(brackets):
    left, right = ['(', '[', '{'], [')', ']', '}']
    mapping = dict(zip(right, left))
    stack = []

    for b in brackets:
        if b in left:
            stack.append(b)
        elif b in right:
            if not stack:
                return False

            top = stack.pop()
            if top != mapping.get(b):
                return False

    return True if len(stack) == 0 else False


if __name__ == '__main__':
    for b in ['([])[]({})', '([)]', '][', '']:
        print('Is "{}" balance? {}'.format(b, '✓' if is_balance(b) else '✗'))
