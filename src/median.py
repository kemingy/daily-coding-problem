# Compute the running median of a sequence of numbers. That is, given a stream 
# of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two 
# middle numbers.


from heapq import heappush, heappop

def sequence_median(seq):
    min_heap, max_heap = [], []

    for s in seq:
        heappush(max_heap, -s)

        heappush(min_heap, -max_heap[0])
        heappop(max_heap)

        if len(max_heap) < len(min_heap):
            heappush(max_heap, -min_heap[0])
            heappop(min_heap)

        if len(max_heap) > len(min_heap):
            yield -max_heap[0]
        else:
            yield (min_heap[0] - max_heap[0]) / 2


if __name__ == '__main__':
    sequence = [2, 1, 5, 7, 2, 0, 5]
    for mid in sequence_median(sequence):
        print('Mid: {}'.format(mid))
