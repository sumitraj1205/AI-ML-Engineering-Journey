# Problem:
# Find the longest common prefix among a list of strings.
#
# Approach:
# Take the first string as the initial prefix.
# Compare it with every other string.
# Keep reducing the prefix until it matches the beginning
# of the current string.
#
# Time Complexity: O(n * m)
# Space Complexity: O(1)
# n = number of strings
# m = length of the prefix


def longest_common_prefix(strs):
    prefix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))