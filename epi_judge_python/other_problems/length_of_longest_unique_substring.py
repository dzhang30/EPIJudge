# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    result = 0
    counters = {}
    for end in range(len(s)):
        current_letter = s[end]
        if current_letter in counters:
            new_start = counters[current_letter] + 1
            for i in range(start, new_start):
                counters.pop(s[i])
            start = new_start

        counters[current_letter] = end

        result = max(result, end - start + 1)

    return result

def lengthOfLongestSubstring2(s: str) -> int:
    result = 0
    head = 0
    tail = 1
    d = {}
    d[s[head]] = 1
    while tail < len(s):
        if s[tail] not in d:
            result = max(result, tail - head + 1)
            d[s[tail]] = 1
        else:
            for i in range(head, tail):
                if s[i] == s[tail]:
                    head = i + 1
                    break
                d.pop(s[i])
        tail += 1

    return result

if __name__ == '__main__':
    s = "abcabcbb"
    result= lengthOfLongestSubstring2(s)
    print(result)