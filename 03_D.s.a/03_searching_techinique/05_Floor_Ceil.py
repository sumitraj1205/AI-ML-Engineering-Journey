# Floor and Ceil in Sorted Array
#
# Problem:
# Given a sorted array and a number X, find:
# Floor = largest element less than or equal to X.
# Ceil = smallest element greater than or equal to X.
#
# Approach:
# Use Binary Search.
# If arr[mid] == X, both floor and ceil are X.
# If arr[mid] < X, it can be a possible floor, so move right.
# If arr[mid] > X, it can be a possible ceil, so move left.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def floor_ceil(arr, x):
    low = 0
    high = len(arr) - 1

    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return arr[mid], arr[mid]

        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1

        else:
            ceil = arr[mid]
            high = mid - 1

    return floor, ceil


arr = [1, 2, 4, 6, 8, 10]
x = 5

floor, ceil = floor_ceil(arr, x)

print("Floor:", floor)
print("Ceil:", ceil)