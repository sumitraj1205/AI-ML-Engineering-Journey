# Count Frequency in a Range
#
# Problem:
# Given an array containing numbers in a specific range,
# count the frequency of every number in that range.
#
# Example:
# Array = [1, 2, 2, 3, 1, 4, 2]
# Range = 1 to 5
#
# Frequency:
# 1 -> 2
# 2 -> 3
# 3 -> 1
# 4 -> 1
# 5 -> 0
#
# Approach:
# Create a frequency array/dictionary for all numbers
# in the required range.
#
# Traverse the input array and increase the frequency
# of each number.
#
# Finally, check the frequency of every number in the range.
#
# Time Complexity: O(n + r)
# Space Complexity: O(r)
#
# n = number of elements in the array
# r = size of the given range


def count_frequency_in_range(arr, low, high):
    frequency = {}

    # Initialize frequency for every number in the range
    for num in range(low, high + 1):
        frequency[num] = 0

    # Count frequency
    for num in arr:
        if low <= num <= high:
            frequency[num] += 1

    return frequency


arr = [1, 2, 2, 3, 1, 4, 2]
low = 1
high = 5

frequency = count_frequency_in_range(arr, low, high)

for num in range(low, high + 1):
    print(num, "->", frequency[num])