# Selection Sort
#
# Problem:
# Given an array, sort the array in ascending order using Selection Sort.
#
# Approach:
# Selection Sort divides the array into a sorted and unsorted part.
# For every position, find the minimum element from the unsorted part
# and swap it with the element at the current position.
#
# Time Complexity:
# Best Case: O(n²)
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Space Complexity: O(1)


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

print(selection_sort(arr))