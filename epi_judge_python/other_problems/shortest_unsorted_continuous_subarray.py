# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.

# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

def findUnsortedSubarray(nums):
    left_stack = []
    left_most_index = float('inf')
    for i in range(len(nums)):
        while left_stack and nums[left_stack[-1]] > nums[i]:
            j = left_stack.pop()
            if j < left_most_index:
                left_most_index = j
        left_stack.append(i)

    right_stack = []
    right_most_index = float('-inf')
    for i in range(len(nums) - 1, -1, -1):
        while right_stack and nums[right_stack[-1]] < nums[i]:
            j = right_stack.pop()
            if j > right_most_index:
                right_most_index = j
        right_stack.append(i)


if __name__ == '__main__':
    nums = [1, 3, 4, 25, 10, 2, 15]

    print(findUnsortedSubarray(nums))
