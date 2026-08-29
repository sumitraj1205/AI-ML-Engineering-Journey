# Quick Sort
#
# Problem:
# Given an array, sort the array in ascending order using Quick Sort.
#
# Approach:
# Quick Sort follows the Divide and Conquer approach.
#
# 1. Choose a pivot element.
# 2. Partition the array so that elements smaller than the pivot
#    are placed on the left and larger elements on the right.
# 3. Recursively apply Quick Sort to both parts.
#
# This implementation uses the last element as the pivot.
#
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²)
#
# Space Complexity:
# Average Case: O(log n)
# Worst Case: O(n)


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


arr = [10, 7, 8, 9, 1, 5]

quick_sort(arr, 0, len(arr) - 1)

print(arr)