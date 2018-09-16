# Conway's Game of Life takes place on an infinite two-dimensional board of 
# square cells. Each cell is either dead or alive, and at each tick, the 
# following rules apply:
# •	Any live cell with less than two live neighbours dies. 
# •	Any live cell with two or three live neighbours remains living. 
# •	Any live cell with more than three live neighbours dies. 
# •	Any dead cell with exactly three live neighbours becomes a live cell. 
# A cell neighbours another cell if it is horizontally, vertically, or 
# diagonally adjacent.

# Note that, `print('xxx', end='\r')` can refresh output. (only one line)

from time import sleep


class ConwayGame:
    def __init__(self, row, col, live):
        self.row, self.col = row, col
        self.live = live
        self.display()

    def evolve(self, step):
        for _ in range(step):
            self.transition()
            # sleep(0.1)
            self.display()


    def transition(self):
        alive = set(self.live)
        self.live = []
        for i in range(self.row):
            for j in range(self.col):
                square_live = sum([1 if nb in alive else 0 for nb in self.neighbours(i, j)])
                if (i, j) in alive and 3 <= square_live <=4:
                    self.live.append((i, j))
                elif (i, j) not in alive and square_live == 3:
                    self.live.append((i, j))


    def neighbours(self, x, y):
        return filter(lambda point: 0 <= point[0] < self.row and 0 <= point[1] < self.col, [
            (a, b) for a in range(x-1, x+2) for b in range(y-1, y+2)
        ])


    def display(self,):
        # live: '*', dead: '.'
        live = set(self.live)
        print()
        for i in range(self.row):
            print(''.join(['*' if (i, j) in live else '.' for j in range(self.col)]))



if __name__ == '__main__':
    live = [(0, 0), (2, 3), (1, 1), (5, 8), (2, 5), (4, 7), (0, 2)]
    game = ConwayGame(10, 10, live)
    game.evolve(10)
