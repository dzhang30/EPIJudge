from collections import deque

# def zigzagTraverse(array):
#     result = {}
#     temp = deque()
#
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             z = i + j
#             if z in result:
#                 if z % 2 == 0:
#                     result[z].append(array[i][j])
#                 else:
#                     result[z].appendleft(array[i][j])
#             else:
#                 result[z] = deque([array[i][j]])
#
#     final = []
#     for k, v in result.items():
#         final.extend(v)
#
#     return final

def zigzagTraverse(array):
    result = []
    indices = deque([])
    arr_length = len(array)
    arr_width = len(array[0])
    target_result_size = arr_length * arr_width

    cur_iteration = 0
    while len(result) != target_result_size:
        remove_count = 0
        for index in indices:
            if index[1] + 1 > arr_width - 1:
                remove_count += 1
            else:
                index[1] = index[1] + 1

        for i in range(remove_count):
            indices.popleft()

        if cur_iteration < arr_length:
            indices.append([cur_iteration, 0])

        for i in range(len(indices)):
            access_index = i if cur_iteration % 2 == 0 else len(indices) - 1 - i
            result.append(array[indices[access_index][0]][indices[access_index][1]])

        cur_iteration += 1

    return result


if __name__ == '__main__':
    test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
    test_2 = [[1]]
    test_3 = [[1, 2, 3, 4, 5]]
    test_4 = [[1], [2], [3], [4], [5]]
    test_5 = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
    print(zigzagTraverse(test))

    d = deque([1])
    d.a