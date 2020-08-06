# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for c in string:
            c_position = ord(c) - ord('a')
            count[c_position] += 1
        result[tuple(count)].append(string)
    print(type(result.values()))
    print(result.values())
    return result


if __name__ == '__main__':
    x = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(groupAnagrams(x))
