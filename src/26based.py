# Spreadsheets often use this alphabetical encoding for its columns: "A", "B",
# "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

# Given a column number, return its alphabetical column id. For example, given
# 1, return "A". Given 27, return "AA".


def convert26to10(alpha):
    num = 0
    for a in alpha[::-1]:
        num = num * 26 + ord(a) - 64

    return num


if __name__ == "__main__":
    for alpha in ["A", "B", "C", "AA", "AB", "ZZ", "AAA", "AAB"]:
        print(alpha, convert26to10(alpha))
