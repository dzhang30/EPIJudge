def minDominoRotations(A, B):
    def minDominoRotationsHelper(A, B, index, count, is_swapped=False):
        if index == len(A) - 1:
            if A[index] == A[index - 1]:
                return count + 1
            else:
                return -1
        else:
            if index == 0:
                temp_count = 0
            elif A[index] == A[index - 1]:
                temp_count = count + 1 if is_swapped else count
            else:
                temp_count = -1

        swapped_A = A.copy()
        swapped_A[index] = B[index]

        if temp_count == -1:
            if is_swapped:
                swapped_count = -1
                unswapped_count = minDominoRotationsHelper(A, B, index + 1, count, is_swapped=False)
            else:
                unswapped_count = -1
                swapped_count = minDominoRotationsHelper(swapped_A, B, index + 1, count + 1, is_swapped=True)
        else:
            unswapped_count = minDominoRotationsHelper(A, B, index + 1, temp_count, is_swapped=False)
            swapped_count = minDominoRotationsHelper(swapped_A, B, index + 1, temp_count, is_swapped=True)

        if unswapped_count == -1 and swapped_count == -1:
            return -1
        elif unswapped_count == -1:
            return swapped_count
        elif swapped_count == -1:
            return unswapped_count
        else:
            return min(swapped_count, unswapped_count)

    return minDominoRotationsHelper(A, B, 0, 0)

if __name__ == '__main__':
    A = [1, 3, 4, 3]
    B = [3, 1, 3, 1]
    import functools
    print([set(d) for d in zip(A, B)])
    s = functools.reduce(set.__and__, [set(d) for d in zip(A, B)])

    print({1, 3}.intersection({3, 4}))

    print(s)