# max non-adjacent sum of array

def max_sum(array):
    prev_one, prev_two, ans = 0, 0, 0

    for i in range(len(array)):
        if i == 0:
            ans = array[0]
        elif i == 1:
            ans = max(array[0], array[1])
        else:
            ans = max(prev_one, prev_two + array[i])

        prev_two = prev_one
        prev_one = ans

    return ans

if __name__ == '__main__':
    array = [2, 1, 4, 5, 8, 2]
    print(max_sum(array))
