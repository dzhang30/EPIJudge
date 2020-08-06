# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,
# 100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from collections import defaultdict, deque
from copy import copy


def findAnagrams(s: str, p: str):
    letter_counts = defaultdict(int)
    for letter in p:
        letter_counts[letter] += 1

    result = []
    letter_counts_copy = copy(letter_counts)
    sliding_window = deque()
    for index, letter in enumerate(s):
        if letter in letter_counts_copy:
            while sliding_window and letter_counts_copy[letter] - 1 < 0:
                popped_index = sliding_window.popleft()
                popped_letter = s[popped_index]
                letter_counts_copy[popped_letter] += 1
                if popped_letter == letter:
                    break
            sliding_window.append(index)
            letter_counts_copy[letter] -= 1
        else:
            sliding_window.clear()
            letter_counts_copy = copy(letter_counts)

        if len(sliding_window) == len(p):
            result_index = sliding_window.popleft()
            result_letter = s[result_index]
            letter_counts_copy[result_letter] += 1
            result.append(result_index)

    return result


def findAnagrams2(s: str, p: str):
    letter_count = defaultdict(int)
    for letter in p:
        letter_count[letter] += 1

    result = []
    target_length = len(p)
    start = 0
    end = 0
    temp_letter_count = defaultdict(int)
    while end < len(s):
        cur_letter = s[end]
        temp_letter_count[cur_letter] += 1
        if end - target_length >= 0:
            pop_index = end - target_length
            pop_letter = s[pop_index]
            if pop_letter in letter_count:
                temp_letter_count[pop_letter] -= 1
            elif pop_letter in temp_letter_count:
                temp_letter_count.pop(pop_letter)
            start += 1

        if temp_letter_count == letter_count:
            result.append(start)

        end += 1

    return result

def findAnagrams3(s: str, p: str):
    counts = defaultdict(int)
    for letter in p:
        counts[letter] += 1

    result = []
    temp_counts = defaultdict(int)
    for i, letter in enumerate(s):
        temp_counts[letter] += 1

        if i >= len(p):
            pop_index = i - len(p)
            pop_letter = s[pop_index]
            if pop_letter in p:
                temp_counts[pop_letter] -= 1
            else:
                if pop_letter in temp_counts:
                    temp_counts.pop(pop_letter)

        if temp_counts == counts:
            result.append(i - (len(p) - 1))

    return result


if __name__ == '__main__':
    string = 'beeaaedcbc'
    target = 'c'

    result = findAnagrams3(string, target)

    print(result)
