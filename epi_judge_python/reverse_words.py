import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words_helper(s, begin, end):
    while begin <= end:
        s[begin], s[end] = s[end], s[begin]
        begin += 1
        end -= 1


def reverse_words(s):
    i = 0
    j = len(s) - 1
    start = i
    end = j

    while i <= j:
        left = chr(s[i])
        right = chr(s[j])

        s[i], s[j] = s[j], s[i]
        if left == ' ':
            reverse_words_helper(s, j + 1, end)
            end = j - 1
        if right == ' ':
            reverse_words_helper(s, start, i - 1)
            start = i + 1

        i += 1
        j -= 1

    reverse_words_helper(s, start, end)

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
    #                                    reverse_words_wrapper))

    s = bytearray('danaiel', 'utf-8')
    # reverse_words(s)
    # print(s)
    reverse_words_helper(s, 0, len(s) - 1)
    print(s)
