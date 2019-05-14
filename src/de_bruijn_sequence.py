# Given a set of characters C and an integer k, a De Bruijn sequence is a
# cyclic sequence in which every possible k-length string of characters in C
# occurs exactly once.

# For example, suppose C = {0, 1} and k = 3. Then our sequence should contain
# the substrings {'000', '001', '010', '011', '100', '101', '110', '111'},
# and one possible solution would be 00010111.

# Create an algorithm that finds a De Bruijn sequence.


def get_substrings(chars, n, substrings=None):
    if n == 0:
        return substrings
    if substrings is None:
        return get_substrings(chars, n-1, [str(c) for c in chars])
    return get_substrings(chars, n-1, ['{}{}'.format(sub, c)
                                       for sub in substrings for c in chars])


def de_bruijn_sequence(chars, n):
    substrings = get_substrings(chars, n)
    m = len(substrings)
    map_out = {}
    for string in substrings:
        map_out[string] = list('{}{}'.format(string[1:], c) for c in chars)

    legal_path = []

    def search(string, path=None):
        if path is None:
            path = [string]
        if len(path) == m:
            legal_path.append(path)
        return [search(s, path+[s]) for s in map_out[string] if s not in path]

    search(substrings[0])
    return ''.join([s[0] for s in legal_path[0]]) if legal_path else ''


if __name__ == "__main__":
    for chars, n in [({0, 1}, 3), ({'+', '-'}, 4), ({0, 1}, 4)]:
        print(de_bruijn_sequence(chars, n))
