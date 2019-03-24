# You come across a dictionary of sorted words in a language you've never seen
# before. Write a program that returns the correct order of letters in this
# language.

# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return
# ['x', 'z', 'w', 'y'].


def get_order(words):
    order = []
    for i in range(len(words) - 1):
        x, y = compare(words[i], words[i+1])
        if x is None:
            continue
        if x not in order:
            if y not in order:
                order.append(x)
                order.append(y)
            else:
                order.insert(order.index(y), x)
        else:
            if y not in order:
                order.append(y)
            else:
                ix, iy = order.index(x), order.index(y)
                if ix > iy:
                    order[ix] = y
                    order[iy] = x

    return order

def compare(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            return x[i], y[i]
    return None, None

if __name__ == '__main__':
    for words in [
        ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
        ['baa', 'abcd', 'abca', 'cab', 'cad'],
        ['caa', 'aaa', 'aab'],
    ]:
        print(get_order(words))
