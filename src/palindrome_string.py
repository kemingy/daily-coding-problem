# Given a string, find the palindrome that can be made by inserting the fewest 
# number of characters as possible anywhere in the word. If there is more than 
# one palindrome of minimum length that can be made, return the 
# lexicographically earliest one (the first one alphabetically).


def shortest_palindrome(word):
    n = len(word)

    # split to (mid, left, right)
    candidates = set()
    for mid in range(n):
        candidates.add((word[mid], word[:mid], word[mid + 1:]))
        candidates.add(('', word[:mid], word[mid:]))

    def get_palindrome(mid, left, right):
        if not left or not right:
            return right[::-1] + left + mid + right + left[::-1]

        if left[-1] == right[0]:
            return get_palindrome(right[0] + mid + right[0], left[:-1], right[1:])

        # add left char or right char to mid string
        add_left = get_palindrome(left[-1] + mid + left[-1], left[:-1], right)
        add_right = get_palindrome(right[0] + mid + right[0], left, right[1:])

        # 1. shortest  2. lexicographically esrliest
        if len(add_left) == len(add_right):
            return min(add_left, add_right)
        return (add_left, add_right)[len(add_left) > len(add_right)]

    palindromes = [get_palindrome(mid, left, right) for mid, left, right in candidates]
    shortest = min(map(len, palindromes))
    return min(filter(lambda x: len(x) == shortest, palindromes))


if __name__ == '__main__':
    for word in ['race', 'google', 'level']:
        palin = shortest_palindrome(word)
        print('Origin: {} \t Palindrome: {} \t Distance: {}'.format(
            word, palin, len(palin) - len(word)))
