# Given a year in the format 'YYYY', count how many palindrome date 'MM/DD/YYYY'

from calendar import monthrange


def palindrome_date(year):
    return len(list(filter(lambda x: x == x[::-1],
                           ['{:02d}{:02d}{}'.format(m, d, year)
                            for m in range(1, 13)
                            for d in range(1, monthrange(year, m)[1])])))


if __name__ == '__main__':
    for year in [2010, 2019, 2020, 2011, 2039, 2090]:
        print(palindrome_date(year))
