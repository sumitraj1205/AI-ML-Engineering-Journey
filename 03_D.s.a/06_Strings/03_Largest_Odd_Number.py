# Problem:
# Find the largest odd number that can be obtained as a substring
# from a given numeric string.
#
# Approach:
# An odd number must end with an odd digit.
# Traverse the string from right to left.
# The first odd digit found becomes the ending position of the answer.
# Return the string from the beginning up to that position.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def largest_odd_number(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[:i + 1]

    return ""


s = "35427"
print(largest_odd_number(s))