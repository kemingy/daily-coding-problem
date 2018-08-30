# Given an array of time intervals (start, end) for classroom lectures (possibly 
# overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def min_classroom(intervals):
    if not intervals:
        return 0

    rooms = [[]]
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        found = False
        for room in rooms:
            if not room or room[-1][1] < interval[0]:
                room.append(interval)
                found = True

        if not found:
            rooms.append([interval])

    for i, room in enumerate(rooms):
        print('Classroom No.{}: {}'.format(i + 1, room))

    return len(rooms)



if __name__ == '__main__':
    intervals = [
        (30, 75),
        (0, 50),
        (60, 150),
        (10, 15),
    ]

    print('Minimum number of rooms: {}'.format(min_classroom(intervals)))

