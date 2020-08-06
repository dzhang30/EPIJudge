# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1]

from pprint import pprint


def next_permutation(nums):
    target_index = -1
    for i in reversed(range(len(nums) - 1)):
        prev_num = nums[i + 1]
        cur_num = nums[i]
        if prev_num > cur_num:
            target_index = i
            break

    if target_index == -1:
        nums.reverse()
        return nums

    target_num = nums[target_index]
    smallest_num_thats_bigger_than_target_num = 100000
    swap_index = -1
    for i in range(target_index + 1, len(nums)):
        cur_num = nums[i]
        if cur_num > target_num and cur_num <= smallest_num_thats_bigger_than_target_num:
            smallest_num_thats_bigger_than_target_num = cur_num
            swap_index = i

    nums[target_index], nums[swap_index] = nums[swap_index], nums[target_index]

    nums[target_index + 1:] = nums[len(nums)-1:target_index:-1]

    return nums


if __name__ == '__main__':
    nums = [2,3,1,3,3]
    result = next_permutation(nums)
    pprint(result)
