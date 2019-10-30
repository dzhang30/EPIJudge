from test_framework import generic_test


def apply_permutation(perm, A):
    for i in range(len(A)):
        while i != perm[i]:
            temp = A[perm[i]]
            A[perm[i]] = A[i]
            A[i] = temp

            temp_p = perm[i]
            perm[i] = perm[temp_p]
            perm[temp_p] = temp_p

    return A



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
