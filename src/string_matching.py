# Implement an efficient string matching algorithm.

# That is, given a string of length N and a pattern of length k, write a
# program that searches for the pattern in the string with less than O(N * k)
# worst-case time complexity.

# If the pattern is found, return the start index of its location.
# If not, return False.


def boyer_moore(string, pattern):
    # good suffix
    suffix = {}
    n = len(pattern)
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            equal = True
            for k in range(n-i):
                if pattern[j+k] == pattern[i+k]:
                    continue
                equal = False
                break
            if equal:
                suffix[pattern[i:]] = j
                break

    def find_bad_index(i, j):
        k = j - 1
        while pattern[k] != string[i] and k >= 0:
            k -= 1
        return j - k if k > 0 else j

    def find_good_suffix(i):
        for j in range(i, n):
            if pattern[j:] in suffix:
                return j - suffix[pattern[j:]]
        return 0

    m = len(string)
    i = n - 1
    while i < m:
        shift = 1
        for k in range(n):
            found = True
            if string[i-k] != pattern[n-1-k]:
                bad = find_bad_index(i-k, n-1-k)
                good = find_good_suffix(n-k)
                shift = max(good, bad)
                found = False
                break

        if found:
            return i
        i += shift
    return False


if __name__ == "__main__":
    for s, p in [('this is a simple example', 'example'), ('abcdbcdbcd', 'ba')]:
        print(boyer_moore(s, p))
