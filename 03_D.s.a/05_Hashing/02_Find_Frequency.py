# Find the Frequency
#
# Problem:
# Given an array and a number X, find how many times X
# occurs in the array.
#
# Approach:
# Use a dictionary to store the frequency of every element.
# Then directly access the frequency of X.
#
# If X does not exist in the dictionary, return 0.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)


def find_frequency(arr, x):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency.get(x, 0)


arr = [1, 2, 2, 3, 1, 2, 4, 2]
x = 2

print("Frequency of", x, ":", find_frequency(arr, x))