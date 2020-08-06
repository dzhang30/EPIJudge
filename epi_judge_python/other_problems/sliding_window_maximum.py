# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very
# right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?

from collections import deque
from pprint import pprint


def clear_sliding_window(sliding_window, nums, new_index):
    # if sliding_window and nums[sliding_window[0]] < nums[new_index]:
    #     sliding_window.popleft()
    while sliding_window and sliding_window[0] < new_index:
        if nums[sliding_window[0]] <= nums[new_index]:
            sliding_window.popleft()
        else:
            break

    while sliding_window and nums[sliding_window[-1]] < nums[new_index]:
        sliding_window.pop()


def maxSlidingWindow(nums, k):
    result = []
    sliding_window = deque([], k)

    for i in range(k):
        clear_sliding_window(sliding_window, nums, i)
        sliding_window.append(i)

    if sliding_window:
        result.append(nums[sliding_window[0]])

    for j in range(k, len(nums)):
        if sliding_window and sliding_window[0] < j - k + 1:
            sliding_window.popleft()

        clear_sliding_window(sliding_window, nums, j)

        sliding_window.append(j)
        result.append(nums[sliding_window[0]])

    return result


if __name__ == '__main__':
    nums = [4, 3, 11]
    k = 3

    result = maxSlidingWindow(nums, k)
    print(result)
