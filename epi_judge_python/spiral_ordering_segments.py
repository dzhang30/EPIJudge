from test_framework import generic_test
from pprint import pprint


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    result = []
    length = len(square_matrix)
    if not length:
        return result
    # if length == 1:
    #     return square_matrix[0]
    shift = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    x = 0
    y = 0
    for _ in range(length ** 2):
        result.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        dir_x = x + shift[direction][0]
        dir_y = y + shift[direction][1]
        if not (0 <= dir_x < length and 0 <= dir_y < length and square_matrix[dir_x][dir_y] != 0):
            direction = 0 if direction == 3 else direction + 1
            x = x + shift[direction][0]
            y = y + shift[direction][1]
        else:
            x = dir_x
            y = dir_y

    return result


if __name__ == '__main__':
    # square_matrix = [[1, 4, 7], [9, 8, 2], [3, 5, 6]]
    # matrix_in_spiral_order(square_matrix)
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
