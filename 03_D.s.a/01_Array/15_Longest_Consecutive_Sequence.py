# Longest Consecutive Sequence
#
# Problem:
# Given an unsorted array of integers, find the length
# of the longest sequence of consecutive elements.
#
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Sequence: [1, 2, 3, 4]
# Answer: 4
#
# Approach:
# Store all elements in a set for O(1) average lookup.
#
# A number is the beginning of a sequence if:
#
#     num - 1
#
# does not exist in the set.
#
# Starting from such a number, keep checking the next
# consecutive numbers.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)


def longest_consecutive(arr):
    numbers = set(arr)

    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))