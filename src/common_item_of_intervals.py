# Given a set of closed intervals, find the smallest set of numbers that covers 
# all the intervals. If there are multiple smallest sets, return any of them.

# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of 
# numbers that covers all these intervals is {3, 6}.


def common_items(intervals):
    assert len(intervals) > 0

    sets = []
    base = intervals[0]
    for interval in intervals[1:]:
        overlap = get_overlap(interval, base)
        if not overlap:
            sets.append(base)
            base = interval
        else:
            base = overlap

    sets.append(base)
    return {s[0] for s in sets}


def get_overlap(x, y):
    if x[0] > y[1] or x[1] < y[0]:
        return None
    return [max(x[0], y[0]), min(x[1], y[1])]


if __name__ == '__main__':
    print(common_items([[0, 3], [2, 6], [3, 4], [6, 9]]))
