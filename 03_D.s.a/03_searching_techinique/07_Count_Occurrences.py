# Count Occurrences
#
# Problem:
# Given a sorted array containing duplicate elements,
# count how many times a number X occurs.
#
# Approach:
# Find the first and last occurrence of X.
# Number of occurrences = last index - first index + 1.
# If X is not present, return 0.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def first_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            answer = mid
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return answer


def last_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            answer = mid
            low = mid + 1

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return answer


def count_occurrences(arr, x):
    first = first_occurrence(arr, x)

    if first == -1:
        return 0

    last = last_occurrence(arr, x)

    return last - first + 1


arr = [1, 2, 2, 2, 2, 3, 4]
x = 2

print(count_occurrences(arr, x))