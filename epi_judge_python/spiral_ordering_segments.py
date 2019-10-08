from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    length = len(square_matrix[0])
    width = length - 1
    result = []
    flip = False
    while length > 0 or width > 0:
        for i in range(length):
            for j in range(width):
                result.append()

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
