# Problem:
# Reverse the order of words in a given string.
#
# Approach:
# Split the string into words, reverse the list of words,
# and join them using a single space.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def reverse_words(s):
    words = s.split()
    words.reverse()

    return ' '.join(words)


s = "the sky is blue"
print(reverse_words(s))