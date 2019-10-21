from typing import List


def removeElement(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    tail = len(nums) - 1
    i = 0
    while i <= tail:
        if nums[i] == val:
            cur_val = nums[i]
            nums[i] = nums[tail]
            nums[tail] = cur_val
            tail -= 1
        else:
            i += 1

    return i


def removeElement2(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i

def removeElement3(nums: List[int], val: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3

    result = removeElement(nums, val)

    print(f'result: {result}, nums: {nums}')

    nums2 = [3,2 , 2, 3]
    val2 = 3

    result2 = removeElement2(nums2, val2)

    print(f'result: {result2}, nums: {nums2}')