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
    def is_match(string: str, pattern: str, i: int, j: int):
        if j == len(pattern):
            return i == len(string)

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            if i < len(string) and (string[i] == pattern[j] or pattern[j] == '.'):
                keep_string_advance_pattern = is_match(string, pattern, i, j + 2)
                advance_string_keep_pattern = is_match(string, pattern, i + 1, j)
                return keep_string_advance_pattern or advance_string_keep_pattern
            else:
                keep_string_advance_pattern = is_match(string, pattern, i, j + 2)
                return keep_string_advance_pattern
        else:
            if i < len(string) and string[i] == pattern[j] or pattern[j] == '.':
                advance_string_and_pattern = is_match(string, pattern, i + 1, j + 1)
                return advance_string_and_pattern
            else:
                return False

    return is_match(s, p, 0, 0)


if __name__ == '__main__':
    s = 'mississippi'
    p = 'mis*is*p*.'
    assert isMatch(s, p) is False

    s = 'aab'
    p = 'c*a*b'
    assert isMatch(s, p) is True

    s = 'aa'
    p = 'a'
    assert isMatch(s, p) is False

    s = 'ab'
    p = '.*'
    assert isMatch(s, p) is True

    s = 'ab'
    p = '.*ab'
    assert isMatch(s, p) is True

    s = 'ab'
    p = '.*c'
    assert isMatch(s, p) is False

    s = 'aaa'
    p = 'aaaa'
    assert isMatch(s, p) is False

    s = ""
    p = "c*c*"
    assert isMatch(s, p) is True

    s = 'a'
    p = 'ab*'
    assert isMatch(s, p) is True

    s = 'aabcbcbcaccbcaabc'
    p = '.*a*aa*.*b*.c*.*a*'
    assert isMatch(s, p) is True

    s = 'bbbba'
    p = '.*a*a'
    assert isMatch(s, p) is True