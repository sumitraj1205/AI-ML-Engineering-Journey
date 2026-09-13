# Problem:
# Check whether two strings are anagrams of each other.
#
# Approach:
# Count the frequency of every character in both strings.
# If the frequency dictionaries are equal, the strings are anagrams.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in t:
        if ch not in frequency:
            return False

        frequency[ch] -= 1

        if frequency[ch] < 0:
            return False

    return True


s = "listen"
t = "silent"

print(is_anagram(s, t))