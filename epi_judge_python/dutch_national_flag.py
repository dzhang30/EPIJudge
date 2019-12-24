import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.
    lower_index = 0
    mid_index = 0
    upper_index = len(A) - 1

    pivot_val = A[pivot_index]
    while mid_index <= upper_index:
        if A[mid_index] < pivot_val:
            swap(A, lower_index, mid_index)
            lower_index += 1
            mid_index += 1
        elif A[mid_index] > pivot_val:
            swap(A, mid_index, upper_index)
            upper_index -= 1
        else:
            mid_index += 1

    return A

def swap(arr, index_one, index_two):
    temp = arr[index_one]
    arr[index_one] = arr[index_two]
    arr[index_two] = temp

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
