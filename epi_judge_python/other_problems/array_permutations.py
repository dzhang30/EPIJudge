from pprint import pprint


# O(n*n!) time | O(n*n!) space
# def getPermutations(array):
#     permutations = []
#     permutationsHelper(0, array, permutations)
#     return permutations
#
#
# def permutationsHelper(i, array, permutations):
#     if i == len(array) - 1:
#         permutations.append(array[:])
#     else:
#         for j in range(i, len(array)):
#             swap(array, i, j)
#             permutationsHelper(i + 1, array, permutations)
#             swap(array, i, j)
#
#
# def swap(array, i, j):
#     array[i], array[j] = array[j], array[i]


def getPermutations(array):
    def perm_helper(arr, perm, result):
        if len(arr) == 0:
            result.append(perm)
        else:
            for i in range(len(arr)):
                num = arr[i]
                new_arr = arr[0:i] + arr[i + 1:len(arr)]
                new_perm = perm + [num]
                perm_helper(new_arr, new_perm, result)

    if len(array) == 0:
        return []

    result = []
    perm_helper(array, [], result)
    return result


if __name__ == '__main__':
    arr = []
    pprint(getPermutations(arr))
