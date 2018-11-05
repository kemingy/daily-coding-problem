# Implement division of two positive integers without using the division, 
# multiplication, or modulus operators. Return the quotient as an integer, 
# ignoring the remainder.

def division(divident, divisor):
    quotient = 0
    if divident == 0:
        return 0
    elif divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    tmp = 0
    for i in range(31, -1, -1):
        if tmp + (divisor << i) <= divident:
            tmp += (divisor << i)
            quotient |= (1 << i)

    return quotient


if __name__ == '__main__':
    for x, y in [(0, 2), (4, 2), (1000000, 1), (5, 3), (20, 7), (30, 3), (2, 0)]:
        print('{} ÷ {} = {}'.format(x, y, division(x, y)))