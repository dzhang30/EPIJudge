# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]


def duplicateZeros(arr) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    zeros = arr.count(0)

    for i in range(len(arr) - 1, -1, -1):
        if i + zeros < len(arr):
            arr[i + zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < len(arr):
                arr[i + zeros] = 0

    return arr

if __name__ == '__main__':
    arr = [8,4,5,0,0,0,0,7]
    result = duplicateZeros(arr)
    print(result)
