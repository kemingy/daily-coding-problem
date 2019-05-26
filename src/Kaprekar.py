# The number 6174 is known as Kaprekar's contant, after the mathematician who
# discovered an associated property: for all four-digit numbers with at least
# two distinct digits, repeatedly applying a simple procedure eventually
# results in this value. The procedure is as follows:

# •	For a given input x, create two new numbers that consist of the digits in
# x in ascending and descending order.
# •	Subtract the smaller number from the larger number.

# For example, this algorithm terminates in three steps when starting from 1234:
# •	4321 - 1234 = 3087
# •	8730 - 0378 = 8352
# •	8532 - 2358 = 6174
# Write a function that returns how many steps this will take for a given
# input N.


def kaprekar_step(num):
    count = 0
    while num != 6174:
        chars = list(str(num))
        num = int(''.join(sorted(chars, reverse=True))) - \
            int(''.join(sorted(chars)))
        count += 1

    return count


if __name__ == "__main__":
    for num in [2134, 5639, 9983, 4658]:
        print(num, kaprekar_step(num))
