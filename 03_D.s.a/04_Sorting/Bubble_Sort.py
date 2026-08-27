# Bubble Sort
#
# Problem:
# Given an array, sort the array in ascending order using Bubble Sort.
#
# Approach:
# Compare adjacent elements.
# If the left element is greater than the right element, swap them.
# After every pass, the largest unsorted element moves to its correct position.
#
# The swapped flag is used to stop early if the array is already sorted.
#
# Time Complexity:
# Best Case: O(n)
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Space Complexity: O(1)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))