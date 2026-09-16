# Problem:
# Sort the characters of a string in decreasing order of their frequency.
#
# Approach:
# First count the frequency of each character using a dictionary.
# Then sort the characters according to their frequency.
# Finally, add each character frequency times.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)


def frequency_sort(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    sorted_chars = sorted(frequency, key=frequency.get, reverse=True)

    result = ""

    for ch in sorted_chars:
        result += ch * frequency[ch]

    return result


s = "tree"

print(frequency_sort(s))