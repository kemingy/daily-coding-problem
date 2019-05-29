# A teacher must divide a class of students into two teams to play dodgeball.
# Unfortunately, not all the kids get along, and several refuse to be put on
# the same team as that of their enemies.

# Given an adjacency list of students and their enemies, write an algorithm
# that finds a satisfactory pair of teams, or returns False if none exists.

# For example, given the following enemy graph you should return the teams
# {0, 1, 4, 5} and {2, 3}.

# students = {
# 0: [3],
# 1: [2],
# 2: [1, 4],
# 3: [0, 4, 5],
# 4: [2, 3],
# 5: [3]
# }

# On the other hand, given the input below, you should return False.

# students = {
# 0: [3],
# 1: [2],
# 2: [1, 3, 4],
# 3: [0, 2, 4, 5],
# 4: [2, 3],
# 5: [3]
# }


class Team:
    def __init__(self):
        self.members = set()
        self.enemies = set()

    def add(self, student, enemies):
        self.members.add(student)
        self.enemies |= set(enemies)

    def __repr__(self):
        return '<{}>'.format(', '.join([str(m) for m in self.members]))


def build_team(adjacency):
    x, y = Team(), Team()
    for student, enemies in adjacency.items():
        if not x:
            x.add(student, enemies)
        elif not y:
            y.add(student, enemies)
        elif student not in x.enemies:
            x.add(student, enemies)
        elif student not in y.enemies:
            y.add(student, enemies)

    if len(x.members) + len(y.members) == len(adjacency):
        return x, y
    return False


if __name__ == "__main__":
    for adj in [{
        0: [3],
        1: [2],
        2: [1, 4],
        3: [0, 4, 5],
        4: [2, 3],
        5: [3]
    }, {
        0: [3],
        1: [2],
        2: [1, 3, 4],
        3: [0, 2, 4, 5],
        4: [2, 3],
        5: [3]
    }]:
        print(build_team(adj))
