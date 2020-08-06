from pprint import pprint
from collections import defaultdict, deque


def diagonal_traverse(matrix):
    result_dict = defaultdict(deque)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            result_dict[row + col].appendleft(matrix[row][col])

    result = []
    for k, v in result_dict.items():
        result.extend(v)
    return result

#
# def diagonal_traverse(matrix):
#     pass


if __name__ == '__main__':
    test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(diagonal_traverse(test))
