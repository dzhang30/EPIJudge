# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

def binary_search_range(nums, target, is_right):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        cur_val = nums[mid]

        if (cur_val == target and is_right) or cur_val < target:
            left = mid + 1
        elif (cur_val == target and not is_right) or cur_val > target:
            right = mid - 1
    return left


def searchRange(nums, target):
    result = [-1, -1]

    left = binary_search_range(nums, target, is_right=True)
    print(left)

    return result


if __name__ == '__main__':
    nums = [0, 5, 5, 5, 5, 9]
    target = 5

    searchRange(nums, target)
