# Recursive Bubble Sort
#
# Problem:
# Given an array, sort the array in ascending order using
# the recursive version of Bubble Sort.
#
# Approach:
# Perform one Bubble Sort pass to move the largest element
# to the end of the unsorted portion.
#
# After each pass, recursively call the function for the
# remaining unsorted portion.
#
# Base Case:
# If the size of the unsorted portion is 1 or less,
# the array is already sorted.
#
# Time Complexity:
# Best Case: O(n) with optimization
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Space Complexity: O(n) due to recursion stack


def recursive_bubble_sort(arr, n):

    if n <= 1:
        return

    swapped = False

    for i in range(n - 1):

        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    if not swapped:
        return

    recursive_bubble_sort(arr, n - 1)


arr = [64, 34, 25, 12, 22, 11, 90]

recursive_bubble_sort(arr, len(arr))

print(arr)