# Connect 4 is a game where opponents take turns dropping red or black discs
# into a 7 x 6 vertically suspended grid. The game ends either when one player
# creates a line of four consecutive discs of their color (horizontally,
# vertically, or diagonally), or when there are no more spots left in the grid.


from enum import Enum
from random import randint


class Disc(Enum):
    RED = 0
    BLACK = 1


class Connect4:
    def __init__(self):
        self.nrow = 7
        self.ncol = 6
        self.grid = [[None for i in range(self.ncol)]
                     for j in range(self.nrow)]
        self.winner = None
        self.discs = ("⦾", "◼")

    def reset(self):
        self.grid = [[None for i in range(self.ncol)]
                     for j in range(self.nrow)]
        self.winner = None

    def continue4(self, x, y):
        length = min(len(x), len(y))
        if length < 4:
            return False

        count = 0
        pre = self.grid[x[0]][y[0]]
        for i in range(1, min(len(x), len(y))):
            cur = self.grid[x[i]][y[i]]
            if cur and cur == pre:
                count = 2 if count == 0 else count + 1
            else:
                count = 0
            if count >= 4:
                self.winner = cur
                return True
            pre = cur
        return False

    def is_full(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.grid[i][j] is None:
                    return False
        return True

    def is_over(self):
        if self.is_full():
            return True

        horizontally = any([self.continue4(
            [x for i in range(self.ncol)], [j for j in range(self.ncol)])
            for x in range(self.nrow)])
        if horizontally:
            return True

        vertically = any([self.continue4(
            [i for i in range(self.nrow)], [y for j in range(self.nrow)])
            for y in range(self.ncol)])
        if vertically:
            return True

        diagonally = any([self.continue4(
            [i for i in range(self.nrow)], [j for j in range(start, self.ncol)]
        ) for start in range(self.ncol)] + [self.continue4(
            [i for i in range(start, self.nrow)], [j for j in range(self.ncol)]
        ) for start in range(self.nrow)] + [self.continue4(
            [i for i in range(self.nrow)], [j for j in range(start, -1, -1)]
        ) for start in range(self.ncol - 1, -1, -1)] + [self.continue4(
            [i for i in range(start, self.nrow)], [
                j for j in range(self.ncol - 1, -1, -1)]
        ) for start in range(self.nrow)]
        )
        if diagonally:
            return True

        return False

    def display(self):
        print("-" * 13)
        for row in self.grid:
            print(
                " ".join(["{}" for _ in range(6)]).format(
                    *[
                        self.discs[row[i].value] if row[i] is not None else "◻"
                        for i in range(6)
                    ]
                ),
                end=" |\n",
            )
        print("-" * 13)

    def put(self, i, j, disc=0):
        if 0 <= i < 7 and 0 <= j < 6:
            if self.grid[i][j] is None:
                if disc == 0 or disc == 1:
                    self.grid[i][j] = Disc.RED if disc == 0 else Disc.BLACK
                    return True
        return False


if __name__ == "__main__":
    c4 = Connect4()
    step = 0
    while not c4.is_over():
        while not c4.put(randint(0, 6), randint(0, 5), step & 1):
            continue

        c4.display()
        step += 1

    if c4.winner:
        print('Winner is {}'.format(c4.winner))
    else:
        print('Draw.')
