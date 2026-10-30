# Problem: Print all subsequences whose sum is equal to K.
# Approach: Use take and not-take recursion.
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) auxiliary recursion space.

def subsequences_sum_k(index, arr, current, total, k):
    if index == len(arr):
        if total == k:
            print(current)
        return

    # Take the current element
    current.append(arr[index])
    subsequences_sum_k(
        index + 1, arr, current, total + arr[index], k
    )

    # Do not take the current element
    current.pop()
    subsequences_sum_k(index + 1, arr, current, total, k)


arr = [1, 2, 1]
k = 2

subsequences_sum_k(0, arr, [], 0, k)