# Given an array of strictly the characters 'R', 'G', and 'B', segregate the 
# values of the array so that all the Rs come first, the Gs come second, and 
# the Bs come last. You can only swap elements of the array.


def sort_color(color):
    n = len(color)
    head, tail, current = 0, n - 1, 0

    while current <= tail:
        while color[head] == 'R':
            head += 1

        while color[tail] == 'B':
            tail -= 1

        current = max(current, head)
        if current > tail:
            break

        if color[current] == 'R':
            color[current], color[head] = color[head], color[current]
        elif color[current] == 'B':
            color[current], color[tail] = color[tail], color[current]
        else:
            current += 1

    return color


if __name__ == '__main__':
    for rgb in [['G', 'B', 'R', 'R', 'B', 'R', 'G'], ['G', 'B', 'G', 'B']]:
        print('Origin: "{}" \t Sorted: "{}"'.format(
            '-'.join(rgb), '-'.join(sort_color(rgb))
        ))
