# Problem:
# Check whether two strings are isomorphic.
#
# Approach:
# Each character of the first string must map to exactly one character
# of the second string, and two different characters cannot map
# to the same character.
#
# Use two dictionaries to maintain mapping in both directions.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
            return False

        if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
            return False

        s_to_t[s[i]] = t[i]
        t_to_s[t[i]] = s[i]

    return True


s = "egg"
t = "add"

print(is_isomorphic(s, t))