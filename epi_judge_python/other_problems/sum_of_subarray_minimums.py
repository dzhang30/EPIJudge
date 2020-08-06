# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.

# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

def sumSubarrayMins(A):
    q = []
    result = 0
    prev_sum = 0
    for i in range(len(A)):
        popped = 1
        while q and A[i] < A[q[-1][0]]:
            prev_index, prev_count = q.pop()
            prev_sum -= A[prev_index] * prev_count
            popped += prev_count

        prev_sum += A[i] * popped
        q.append((i, popped))

        result += prev_sum

    return result


if __name__ == '__main__':
    nums = [3, 1, 2, 4, 1]

    print(sumSubarrayMins(nums))
    print(10**9 + 7)
    print(10**9)