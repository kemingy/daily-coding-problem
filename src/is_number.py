# Given a string, return whether it represents a number. Here are the different 
# kinds of numbers:
# •	"10", a positive integer 
# •	"-10", a negative integer 
# •	"10.1", a positive real number 
# •	"-10.1", a negative real number 
# •	"1e5", a number in scientific notation 
# And here are examples of non-numbers:
# •	"a" 
# •	"x 1" 
# •	"a -2" 
# •	"-" 

def is_number(num):
    symbol = None
    integer, decimal = [], []
    sci = None
    SYMBOLS = {'+': 1, '-': -1}

    cur = integer
    for n in num:
        if 48 <= ord(n) <= 57:
            cur.append(n)
        elif n in SYMBOLS and symbol is None:
            symbol = SYMBOLS[n]
        elif n == '.' and cur == integer:
            cur = decimal
        elif n == 'e' and sci is None:
            cur = sci = []
        else:
            return False

    # print('{}{}.{}'.format(symbol, integer, decimal))
    if not integer and not decimal:
        return False

    return True

if __name__ == '__main__':
    for num in ['10', '-10', '10.1', '-10.1', '1e5', 'a', 'x 1', 'a -2', '-', '.8', '+3', '+-2']:
        print('{} is number? {}'.format(num, is_number(num)))