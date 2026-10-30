# Problem: Find all possible subsets of an array.
# Approach: Use bit manipulation to generate every subset.
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n) for storing the result.

def power_set(arr):
    n = len(arr)
    ans = []

    for num in range(1 << n):
        subset = []

        for i in range(n):
            if num & (1 << i):
                subset.append(arr[i])

        ans.append(subset)

    return ans


arr = [1, 2, 3]

print(power_set(arr))