import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # TODO - you fill in here.
    if not A:
        return 0

    i = 0
    for j in range(1, len(A)):
        if A[i] != A[j]:
            i += 1
            A[i] = A[j]

    return i + 1



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))

