def transformArray(arr):
    operations = 0
    temp_array = []

    while True:
        temp_array.append(arr[0])
        for i in range(1, len(arr) - 1):
            prev_element = arr[i - 1]
            next_element = arr[i + 1]
            cur_element = arr[i]

            if cur_element < prev_element and cur_element < next_element:
                temp_array.append(cur_element + 1)
                operations += 1
            elif cur_element > prev_element and cur_element > next_element:
                temp_array.append(cur_element - 1)
                operations += 1
            else:
                temp_array.append(cur_element)

        temp_array.append(arr[-1])
        arr = temp_array
        temp_array = []

        if operations == 0:
            break
        operations = 0

    return arr

if __name__ == '__main__':
    x = [1,6,3,4,3,5]
    print(transformArray(x))