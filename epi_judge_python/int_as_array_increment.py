from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    r_arr = A[::-1]
    carry = True
    for i in range(len(r_arr)):
        if carry:
            sum = r_arr[i] + 1
            if sum > 9:
                r_arr[i] = 0
            else:
                r_arr[i] = sum
                carry = False

    if carry:
        r_arr.append(1)

    return r_arr[::-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
    # A = [9, 9, 9]
    # print(plus_one(A))