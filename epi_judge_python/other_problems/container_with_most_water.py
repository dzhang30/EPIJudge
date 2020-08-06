# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
from pprint import pprint


def max_area(heights):
    left_ptr = 0
    right_ptr = len(heights) - 1
    max_area = -1

    while left_ptr < right_ptr:
        left_height = heights[left_ptr]
        right_height = heights[right_ptr]
        cur_area = min(left_height, right_height) * (right_ptr - left_ptr)
        max_area = max(max_area, cur_area)
        if left_height <= right_height:
            left_ptr += 1
        else:
            right_ptr -= 1

    return max_area


if __name__ == '__main__':
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    heights_2 = [4, 8, 4, 8]
    result = max_area(heights_2)
    print(result)
