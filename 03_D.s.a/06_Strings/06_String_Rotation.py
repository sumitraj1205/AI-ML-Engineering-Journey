# Problem:
# Check whether one string is a rotation of another string.
#
# Approach:
# If two strings are rotations of each other, the second string
# will always be present inside the first string concatenated with itself.
#
# Example:
# s = "abcd"
# s + s = "abcdabcd"
# "cdab" is present in "abcdabcd"
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def is_rotation(s, goal):
    if len(s) != len(goal):
        return False

    return goal in (s + s)


s = "abcd"
goal = "cdab"

print(is_rotation(s, goal))