from test_framework import generic_test


def generate_pascal_triangle(n):
    result = []

    for i in range(n):
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            result.append([1])
            for j in range(len(result[i - 1])):
                if j == len(result[i - 1]) - 1:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j] + result[i-1][j + 1])

    return result

def generate_pascal_triangle2(n):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
