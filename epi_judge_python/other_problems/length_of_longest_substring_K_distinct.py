# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    result = 0
    start = 0
    counters = defaultdict(int)
    for end in range(len(s)):
        cur_letter = s[end]
        counters[cur_letter] += 1

        while len(counters) > k:
            remove_letter = s[start]
            counters[remove_letter] -= 1
            if counters[remove_letter] == 0:
                counters.pop(remove_letter)
            start += 1

        result = max(result, end - start + 1)

    return result


if __name__ == '__main__':
    s = 'aabbac'
    k = 2

    result = lengthOfLongestSubstringKDistinct(s, k)
    print(result)
