# Recursive Insertion Sort
#
# Problem:
# Given an array, sort the array in ascending order using
# the recursive version of Insertion Sort.
#
# Approach:
# Recursively sort the first n-1 elements.
# Then insert the nth element into its correct position
# in the already sorted portion.
#
# Base Case:
# If n <= 1, the array is already sorted.
#
# Time Complexity:
# Best Case: O(n²) for this recursive implementation's
#            straightforward analysis
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Space Complexity: O(n) due to recursion stack


def recursive_insertion_sort(arr, n):

    if n <= 1:
        return

    recursive_insertion_sort(arr, n - 1)

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


arr = [12, 11, 13, 5, 6]

recursive_insertion_sort(arr, len(arr))

print(arr)