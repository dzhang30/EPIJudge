"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


def isMatch(s: str, p: str) -> bool:
    def is_match_recurse(string: str, pattern: str, i: int, j: int):
        if i > len(string) - 1 >= 0:
            return (j == len(pattern) - 2 and pattern[j + 1] == '*') or j > len(pattern) - 1

        if j > len(pattern) - 1:
            return i > len(string) - 1

        if string and (string[i] == pattern[j] or pattern[j] == '.'):
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                return is_match_recurse(string, pattern, i, j + 2) or is_match_recurse(string, pattern, i + 1, j)
            else:
                return is_match_recurse(string, pattern, i + 1, j + 1)

        else:
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                return is_match_recurse(string, pattern, i, j + 2)
            else:
                return False

    return is_match_recurse(s, p, 0, 0)


if __name__ == '__main__':
    # s = 'mississippi'
    # p = 'mis*is*p*.'
    # assert isMatch(s, p) is False
    #
    # s = 'aab'
    # p = 'c*a*b'
    # assert isMatch(s, p) is True
    #
    # s = 'aa'
    # p = 'a'
    # assert isMatch(s, p) is False
    #
    # s = 'ab'
    # p = '.*'
    # assert isMatch(s, p) is True
    #
    # s = 'ab'
    # p = '.*ab'
    # assert isMatch(s, p) is True
    #
    # s = 'ab'
    # p = '.*c'
    # assert isMatch(s, p) is False
    #
    # s = 'aaa'
    # p = 'aaaa'
    # assert isMatch(s, p) is False
    #
    # s = ""
    # p = "c*c*"
    # assert isMatch(s, p) is True
    #
    # s = 'a'
    # p = 'ab*'
    # assert isMatch(s, p) is True

    s = 'aabcbcbcaccbcaabc'
    p = '.*a*aa*.*b*.c*.*a*'
    print(isMatch(s, p))