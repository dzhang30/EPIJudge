# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
# complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    target_counts = defaultdict(int)
    for letter in t:
        target_counts[letter] += 1

    result = ''
    count = len(t)
    start = 0
    for end, letter in enumerate(s):
        if letter in t:
            target_counts[letter] -= 1
            if target_counts[letter] >= 0:
                count -= 1

        while count == 0:
            substring = s[start:end + 1]
            if not result or len(substring) < len(result):
                result = substring

            pop_letter = s[start]
            if pop_letter in t:
                target_counts[pop_letter] += 1
                if target_counts[pop_letter] > 0:
                    count += 1
            start += 1
    return result

def minWindow2(s: str, t: str) -> str:
    d = defaultdict(int)
    for letter in t:
        d[letter] += 1

    result = None
    target_count = len(t)
    current_count = defaultdict(int)
    i, j = 0, 0
    while j < len(s):
        end = s[j]
        if end in d:
            current_count[end] += 1
            if current_count[end] <= d[end]:
                target_count -= 1

        while target_count == 0:
            local_result = s[i:j + 1]
            if result is None or len(local_result) <= len(result):
                result = local_result
            start = s[i]
            if start in d:
                current_count[start] -= 1
                if current_count[start] < d[start]:
                    target_count += 1
            i += 1

        j += 1

    return result if result else ''

if __name__ == '__main__':
    # s = 'aa'
    # t = 'aa'

    s = "ADOBECODEBANC"
    t = "ABC"

    # s = "bbaa"
    # t = "aba"

    result = minWindow2(s, t)
    print(result)

    a = []
    a.pop()