# You are given an array representing the heights of neighboring buildings on
# a city street, from east to west. The city assessor would like you to write
# an algorithm that returns how many of these buildings have a view of the
# setting sun, in order to properly value the street.

# For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since
# the top floors of the buildings with heights 8, 6, and 1 all have an
# unobstructed view to the west.

# Can you do this using just one forward pass through the array?


def setting_sun_view(nums):
    count = 0
    highest = 0
    for h in nums[::-1]:
        if h > highest:
            highest = h
            count += 1

    return count


if __name__ == "__main__":
    nums = [3, 7, 8, 3, 6, 1]
    print(setting_sun_view(nums))
