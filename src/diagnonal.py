# On our special chessboard, two bishops attack each other if they share the 
# same diagonal. This includes bishops that have another bishop located between 
# them, i.e. bishops can attack through pieces.
# You are given N bishops, represented as (row, column) tuples on a M by M 
# chessboard. Write a function to count the number of pairs of bishops that 
# attack each other. The ordering of the pair doesn't matter: (1, 2) is 
# considered the same as (2, 1).


# def bishop_attack(m, bishops):
#     count = 0
#     n = len(bishops)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if abs(bishops[i][0] - bishops[j][0]) == abs(bishops[i][1] - bishops[j][1]):
#                 count += 1

#     return count


def bishop_attack(m, bishops):
    n = len(bishops)
    diag, reve = {}, {}

    for b in bishops:
        diff = b[0] - b[1]
        if diff not in diag:
            diag[diff] = []
        diag[diff].append(b)

        diff = m - 1 - b[1] - b[0]
        if diff not in reve:
            reve[diff] = []
        reve[diff].append(b)

    return n - len(diag) + n - len(reve)


if __name__ == '__main__':
    print(bishop_attack(5, [(0, 0), (1, 2), (2, 2), (4, 0)]))
