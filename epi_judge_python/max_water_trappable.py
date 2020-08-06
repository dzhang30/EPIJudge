from test_framework import generic_test


def calculate_trapping_water(heights):
    # TODO - you fill in here.
    left_max_heights = []
    local_left_max = -1
    for height in heights:
        if height > local_left_max:
            local_left_max = height
        left_max_heights.append(local_left_max)

    right_max_heights = []
    local_right_max = -1
    for height in reversed(heights):
        if height > local_right_max:
            local_right_max = height
        right_max_heights.append(local_right_max)

    water_heights = []
    right_max_heights.reverse()
    for i in range(len(heights)):
        min_height_at_index = min(left_max_heights[i], right_max_heights[i])
        if heights[i] < min_height_at_index:
            water_heights.append(min_height_at_index - heights[i])
        else:
            water_heights.append(0)

    return sum(water_heights)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
