# get the max linked area size

from pprint import pprint

def max_linked_area(area):
    n = len(area)
    label = 2
    count = [0] * (n * n // 2 + 1)

    def search(i, j, label):
        area[i][j] = label
        count[label - 2] += 1
        x = [1, 0, 0, -1]
        y = [0, 1, -1, 0]
        for k in range(4):
            next_x = i + x[k]
            next_y = j + y[k]
            if 0 <= next_x < n and 0 <= next_y < n and area[next_x][next_y] == 1:
                search(next_x, next_y, label)

    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:
                search(i, j, label)
                label += 1

    return max(count)


if __name__ == '__main__':
    area = [
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1],
    ]
    print(max_linked_area(area))
    pprint(area)