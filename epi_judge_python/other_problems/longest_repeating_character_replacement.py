# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
#
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
#
# Find the length of the longest sub-string containing all repeating letters you can get after performing the above
# operations.
#
# Note:
# Both the string's length and k will not exceed 104.

# Example 1:
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.

# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
from collections import defaultdict

def characterReplacement( s: str, k: int) -> int:
    result = 0
    start = 0
    temp_longest = 0
    counts = defaultdict(int)
    for end in range(len(s)):
        cur_letter = s[end]
        counts[cur_letter] += 1
        temp_longest = max(temp_longest, counts[cur_letter])
        if end - start + 1 - temp_longest > k:
            counts[s[start]] -= 1
            start += 1

        result = max(result, end - start + 1)

    return result

if __name__ == '__main__':
    s = "AABABBA"
    k = 1

    result = characterReplacement(s, k)
    print(result)